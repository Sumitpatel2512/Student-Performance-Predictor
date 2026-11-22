
import pandas as pd
import pymysql
from pathlib import Path
from getpass import getpass

# Project paths
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = BASE_DIR / "data" / "student-mat.csv"

# Read dataset
df = pd.read_csv(DATA_FILE, sep=";")

# Rename original dataset column for database mapping
df = df.rename(columns={"sex": "Gender"})

print("Dataset loaded:", len(df), "students")

# MySQL connection
password = getpass("Enter MySQL root password: ")

connection = pymysql.connect(
    host="localhost",
    user="root",
    password=password,
    database="student_performance_db",
    port=3306
)

try:
    with connection.cursor() as cursor:

        # Get Mathematics course ID
        cursor.execute(
            "SELECT course_id FROM courses WHERE course_name = %s",
            ("Mathematics",)
        )

        course = cursor.fetchone()

        if course is None:
            raise Exception("Mathematics course not found!")

        course_id = course[0]

        # Clear old imported records
        cursor.execute("DELETE FROM attendance")
        cursor.execute("DELETE FROM results")
        cursor.execute("DELETE FROM students")

        for index, row in df.iterrows():

            # Insert student
            cursor.execute("""
                INSERT INTO students
                (student_code, Gender, age, address, studytime, failures)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                f"MAT{index + 1:03d}",
                row["Gender"],
                int(row["age"]),
                row["address"],
                int(row["studytime"]),
                int(row["failures"])
            ))

            student_id = cursor.lastrowid

            # Insert attendance record
            cursor.execute("""
                INSERT INTO attendance
                (student_id, course_id, absences)
                VALUES (%s, %s, %s)
            """, (
                student_id,
                course_id,
                int(row["absences"])
            ))

            # Calculate pass/fail
            pass_status = 1 if row["G3"] >= 10 else 0

            # Insert examination results
            cursor.execute("""
                INSERT INTO results
                (student_id, course_id, G1, G2, G3, pass_status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                student_id,
                course_id,
                float(row["G1"]),
                float(row["G2"]),
                float(row["G3"]),
                pass_status
            ))

    connection.commit()

    print("\nData imported successfully!")
    print("Students:", len(df))

    with connection.cursor() as cursor:

        cursor.execute("SELECT COUNT(*) FROM students")
        print("Student records:", cursor.fetchone()[0])

        cursor.execute("SELECT COUNT(*) FROM attendance")
        print("Attendance records:", cursor.fetchone()[0])

        cursor.execute("SELECT COUNT(*) FROM results")
        print("Result records:", cursor.fetchone()[0])

        cursor.execute("""
            SELECT Gender, COUNT(*)
            FROM students
            GROUP BY Gender
        """)

        print("\nGender Distribution:")
        for gender, count in cursor.fetchall():
            print(gender, ":", count)

except Exception as error:
    connection.rollback()
    print("Import failed:", error)

finally:
    connection.close()
