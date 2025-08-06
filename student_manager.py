import pandas as pd
from db_connector import get_connection

class StudentManager:
    def __init__(self, config):
        self.config = config

    def get_connection(self):
        return get_connection(self.config)

    def get_merged_data(self):
        try:
            conn = self.get_connection()
            query = """
                SELECT 
                    s.student_id, s.name, s.email, s.phone, s.course_batch, s.department,
                    p.language_used, p.problems_solved,
                    ss.communication_score, ss.mock_interview_score,
                    pl.status AS placement_status
                FROM Student_table s
                JOIN Programming_table p ON s.student_id = p.student_id
                JOIN Soft_skills ss ON s.student_id = ss.student_id
                JOIN Placement_table pl ON s.student_id = pl.student_id
            """
            df = pd.read_sql(query, conn)
            conn.close()

            # Convert to numeric
            df["problems_solved"] = pd.to_numeric(df["problems_solved"], errors="coerce")
            df["communication_score"] = pd.to_numeric(df["communication_score"], errors="coerce")
            df["mock_interview_score"] = pd.to_numeric(df["mock_interview_score"], errors="coerce")

            # Fill missing values with 0
            df.fillna(0, inplace=True)

            # Compute programming score (alias) and overall score
            df["programming_score"] = df["problems_solved"]

            df["overall_score"] = (
                df["programming_score"] * 0.4 +
                df["communication_score"] * 0.3 +
                df["mock_interview_score"] * 0.3
            )

            return df

        except Exception as e:
            print(f"❌ Error loading student data: {e}")
            return pd.DataFrame()

    def get_top_performers(self, category):
        df = self.get_merged_data()
        if category in df.columns:
            return df.nlargest(10, category)[["student_id", "name", category]]
        else:
            print(f"⚠️ Column '{category}' not found.")
            return pd.DataFrame()

    def get_students_by_placement_status(self, status):
        df = self.get_merged_data()
        return df[df["placement_status"] == status]
