from faker import Faker
import random
from tqdm import tqdm
from db_connector import get_connection

def generate_students(config):
    conn = get_connection(config)
    cursor = conn.cursor()

    # Drop and recreate tables
    cursor.execute("DROP TABLE IF EXISTS Placement_table")
    cursor.execute("DROP TABLE IF EXISTS Soft_skills")
    cursor.execute("DROP TABLE IF EXISTS Programming_table")
    cursor.execute("DROP TABLE IF EXISTS Student_table")

    cursor.execute("""
        CREATE TABLE Student_table (
            student_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(100),
            email VARCHAR(100),
            phone VARCHAR(15),
            course_batch VARCHAR(50),
            department VARCHAR(100)
        )
    """)
    cursor.execute("""
        CREATE TABLE Programming_table (
            student_id INT PRIMARY KEY,
            language_used VARCHAR(50),
            problems_solved INT,
            FOREIGN KEY (student_id) REFERENCES Student_table(student_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE Soft_skills (
            student_id INT PRIMARY KEY,
            communication_score INT,
            mock_interview_score INT,
            FOREIGN KEY (student_id) REFERENCES Student_table(student_id)
        )
    """)
    cursor.execute("""
        CREATE TABLE Placement_table (
            student_id INT PRIMARY KEY,
            status VARCHAR(20),
            FOREIGN KEY (student_id) REFERENCES Student_table(student_id)
        )
    """)

    conn.commit()

    # Data generation
    fake = Faker()
    departments = ["Data Science", "Full Stack Development", "AI & ML", "Cyber Security", "Cloud Computing"]
    languages = ["Python", "Java", "C++", "JavaScript", "Go", "Ruby"]

    student_data = []
    prog_data = []
    soft_data = []
    placement_data = []

    for _ in tqdm(range(500), desc="Generating Students"):
        name = fake.name()
        email = fake.email()
        phone = ''.join(random.choices('0123456789', k=10))
        batch = random.choice(["Batch A", "Batch B", "Batch C"])
        dept = random.choice(departments)

        student_data.append((name, email, phone, batch, dept))

    cursor.executemany(
        "INSERT INTO Student_table (name, email, phone, course_batch, department) VALUES (%s, %s, %s, %s, %s)",
        student_data
    )
    conn.commit()

    cursor.execute("SELECT student_id FROM Student_table")
    student_ids = [row[0] for row in cursor.fetchall()]

    for sid in tqdm(student_ids, desc="Assigning Scores"):
        language = random.choice(languages)
        solved = random.randint(50, 500)
        comm_score = random.randint(40, 100)
        mock_score = random.randint(40, 100)
        status = random.choice(["Placed", "Not Placed"])

        prog_data.append((sid, language, solved))
        soft_data.append((sid, comm_score, mock_score))
        placement_data.append((sid, status))

    cursor.executemany(
        "INSERT INTO Programming_table (student_id, language_used, problems_solved) VALUES (%s, %s, %s)",
        prog_data
    )
    cursor.executemany(
        "INSERT INTO Soft_skills (student_id, communication_score, mock_interview_score) VALUES (%s, %s, %s)",
        soft_data
    )
    cursor.executemany(
        "INSERT INTO Placement_table (student_id, status) VALUES (%s, %s)",
        placement_data
    )

    conn.commit()
    cursor.close()
    conn.close()

    print("✅ Successfully generated 500 fake students.")
