import streamlit as st
from db_config import db_config
from generate_fake_students import generate_students
from student_manager import StudentManager
from exporter import export_to_excel
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# Set Streamlit page config
st.set_page_config(page_title="Placement Eligibility App", layout="wide")
st.title("📊 Placement Eligibility App")

# Initialize student manager
manager = StudentManager(db_config)

# ✅ Custom function to display left-aligned tables with filter icons on the right
def show_left_aligned_table(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    
    # Default column settings: left align, enable filter, fix icon to right
    gb.configure_default_column(
        headerClass="left-align-header",
        cellStyle={"textAlign": "left"},
        headerTooltip="Click to filter",
        filter=True
    )

    # Explicitly treat number columns like text for filter alignment fix
    for col in df.select_dtypes(include=["int64", "float64"]).columns:
        gb.configure_column(
            col,
            type=["textColumn"],
            headerClass="left-align-header",
            cellStyle={"textAlign": "left"},
            filter=True
        )

    grid_options = gb.build()

    custom_css = {
        ".left-align-header .ag-header-cell-label": {
            "justify-content": "space-between !important",
            "flex-direction": "row !important",
            "text-align": "left !important"
        },
        ".ag-header-cell-text": {
            "text-align": "left !important",
            "flex-grow": "1"
        },
        ".ag-cell": {
            "text-align": "left !important"
        }
    }

    AgGrid(
        df,
        gridOptions=grid_options,
        fit_columns_on_grid_load=True,
        custom_css=custom_css,
        enable_enterprise_modules=False,
        use_container_width=True
    )

# Section: Generate Data
st.header("🧪 Generate Fake Student Records")
if st.button("Generate 500 Students"):
    generate_students(db_config)
    st.success("✅ Successfully generated 500 fake students!")

# Load merged student data
df = manager.get_merged_data()

if df.empty:
    st.warning("ℹ️ Please generate student records first.")
    st.stop()

# Section: Display All Students
st.header("📄 All Student Records")
show_left_aligned_table(df)

# Section: Filter by Placement Status
st.header("🎯 Filter Students by Placement Status")
status_options = df["placement_status"].unique().tolist()
export_status = st.selectbox("Select Placement Status:", options=status_options)

export_df = manager.get_students_by_placement_status(export_status)
show_left_aligned_table(export_df)

# Export to Excel
if not export_df.empty:
    filename = f"students_{export_status.lower()}.xlsx"
    st.download_button(
        label="📥 Download Filtered Students as Excel",
        data=export_to_excel(export_df, filename),
        file_name=filename,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.warning("⚠️ No data available to export for the selected status.")

# Section: Top 10 Performers
st.header("🏆 Top 10 Performers")
col1, col2 = st.columns(2)

with col1:
    st.subheader("💻 Programming Score")
    top_programming = manager.get_top_performers("programming_score")
    show_left_aligned_table(top_programming)

    st.subheader("🧠 Problems Solved")
    top_problems = manager.get_top_performers("problems_solved")
    show_left_aligned_table(top_problems)

with col2:
    st.subheader("🗣️ Communication Score")
    top_communication = manager.get_top_performers("communication_score")
    show_left_aligned_table(top_communication)

    st.subheader("📊 Overall Performance")
    top_overall = manager.get_top_performers("overall_score")
    show_left_aligned_table(top_overall)
