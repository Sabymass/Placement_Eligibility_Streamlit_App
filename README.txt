## 📊 Placement Eligibility Streamlit App

This is a fully interactive web application built using *Streamlit* to simulate and manage placement eligibility data for students. The app generates 500 fake student records with academic and soft skill metrics, calculates placement eligibility, provides detailed tables, and supports exporting to Excel.

---

## 🚀 Features

- 🎲 *Generate 500 Fake Student Records*  
  Generates a new set of realistic student data using the Faker and random libraries.

- 📋 *Auto-Creates and Populates All Tables*  
  Creates all required database tables (Student, Programming, Soft Skills, Placement) automatically if not present.

- 🔍 *View & Filter Student Data*  
  Display detailed tables for:
  - Student Info  
  - Programming Performance  
  - Soft Skills  
  - Placement Status  

- 🎯 *Top 10 Performer Filters*  
  - Programming (problems solved)
  - Soft Skills (communication + mock scores)
  - Overall Performance (combined)

- 📥 *Download Filtered Data as Excel*  
  Export any table or filtered view to an Excel file.

- ✅ *Filter by Placement Status*  
  Toggle between 'Placed', 'Not Placed', or 'All'.

---

## 🧾 Table Definitions

Each table uses student_id as the *primary key*.

- *Student_table*: name, email, department, batch  
- *Programming_table*: problems solved, programming score  
- *Soft_skills*: communication score, mock interview score  
- *Placement_table*: placement status

---

## 🗂️ Folder Structure

Placement_Eligibility_App/
├── app.py # Main Streamlit app
├── db_config.py # DB configuration (host, user, password)
├── db_connector.py # Connection logic to TiDB
├── generate_fake_students.py # Generates fake 500 student records
├── student_manager.py # Handles data retrieval & queries
├── exporter.py # Exports filtered data to Excel
├── requirements.txt # Python dependencies
└── README.md # You're here!


---

## 🛠️ Setup Instructions

1. *Clone the repository*

```bash
git clone https://github.com/yourusername/Placement_Eligibility_App.git
cd Placement_Eligibility_App
Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Configure your database

Edit db_config.py:

python

DB_CONFIG = {
    'host': 'your_host',
    'user': 'your_user',
    'password': 'your_password',
    'database': 'Student_Info'
}
Make sure the TiDB or MySQL-compatible database is accessible and the credentials are correct.

## Run the Streamlit App

streamlit run app.py

🖼️ Screenshots (Attached for references)
🧾 Main Dashboard

📊 Programming Table

💬 Soft Skills Table

🎯 Top 10 Performers

📥 Export Excel Feature

🧰 Technologies Used
Python 3.9+

Streamlit – Web interface

Pandas – Data processing

Faker – Fake student data

MySQL / TiDB – Database

st-aggrid – Interactive tables

openpyxl – Excel export

tqdm – Progress bar for data generation

🚧 Future Enhancements

✅ Add charts/graphs for placement trends

🧮 Show average scores per department

🔒 Add user authentication (admin vs student)

🌐 Deploy on Streamlit Cloud / Heroku / AWS

👨‍💻 Author
Sabarish Balakrishnan
📧 Email: [sabysabarish65@gmail.com]
🌐 LinkedIn: [https://www.linkedin.com/in/sabarish-balakrishnan/]
📁 GitHub: [https://github.com/Sabymass]

📄 License
This project is licensed under the MIT License. Feel free to use and customize it.