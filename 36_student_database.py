"""
Project 36

Student Database

A command-line student management application built with Python
and SQLite.

Features:
- Add students
- View all students
- Search students by ID
- Update student information
- Delete students
- Store data permanently in a SQLite database

Concepts practiced:
- Functions
- SQLite
- sqlite3 module
- Database connection
- Cursor
- SQL
- CREATE TABLE
- INSERT
- SELECT
- UPDATE
- DELETE
- WHERE
- Parameterized queries
- fetchone()
- fetchall()
- commit()
- Exception handling
- Input validation
- while loops
- if / elif / else
"""


import sqlite3


def connect_database():
    """Connect to the SQLite database and create a cursor."""

    connection = sqlite3.connect("students.db")
    cursor = connection.cursor()

    return connection, cursor


def create_table(connection, cursor):
    """Create the students table if it does not already exist."""

    sql = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        grade REAL
    )
    """

    cursor.execute(sql)
    connection.commit()


def add_student(connection, cursor):
    """Add a new student to the database."""

    while True:
        name = input("Enter Name: ").strip().lower()

        if not name:
            print("Name cannot be empty.")
            continue

        break

    while True:
        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid age. Please enter a number.")

    while True:
        try:
            grade = float(input("Enter Grade: "))

            if grade <= 0:
                print("Grade must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid grade. Please enter a number.")

    sql = """
    INSERT INTO students (name, age, grade)
    VALUES (?, ?, ?)
    """

    cursor.execute(sql, (name, age, grade))
    connection.commit()

    print("Student added successfully.")


def view_students(connection, cursor):
    """Display all students stored in the database."""

    sql = "SELECT * FROM students"

    cursor.execute(sql)

    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\n===== STUDENTS =====")

    for student in students:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Age: {student[2]} | "
            f"Grade: {student[3]}"
        )


def search_student(connection, cursor):
    """Search for a student by ID."""

    while True:
        try:
            student_id = int(input("Enter Student ID: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    sql = "SELECT * FROM students WHERE id = ?"

    cursor.execute(sql, (student_id,))

    student = cursor.fetchone()

    if student:
        print(
            f"ID: {student[0]} | "
            f"Name: {student[1]} | "
            f"Age: {student[2]} | "
            f"Grade: {student[3]}"
        )
    else:
        print("Student not found.")


def update_student(connection, cursor):
    """Update the information of an existing student."""

    while True:
        try:
            student_id = int(input("Enter Student ID: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    sql = "SELECT * FROM students WHERE id = ?"

    cursor.execute(sql, (student_id,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    while True:
        name = input("Enter Name: ").strip().lower()

        if not name:
            print("Name cannot be empty.")
            continue

        break

    while True:
        try:
            age = int(input("Enter Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid age. Please enter a number.")

    while True:
        try:
            grade = float(input("Enter Grade: "))

            if grade <= 0:
                print("Grade must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid grade. Please enter a number.")

    sql = """
    UPDATE students
    SET name = ?, age = ?, grade = ?
    WHERE id = ?
    """

    cursor.execute(
        sql,
        (name, age, grade, student_id)
    )

    connection.commit()

    print("Student updated successfully.")


def delete_student(connection, cursor):
    """Delete a student from the database by ID."""

    while True:
        try:
            student_id = int(input("Enter Student ID: "))

            if student_id <= 0:
                print("Student ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    sql = "SELECT * FROM students WHERE id = ?"

    cursor.execute(sql, (student_id,))

    student = cursor.fetchone()

    if not student:
        print("Student not found.")
        return

    sql = "DELETE FROM students WHERE id = ?"

    cursor.execute(sql, (student_id,))
    connection.commit()

    print("Student deleted successfully.")


def main_menu():
    """Display the main menu and return the user's choice."""

    while True:

        try:
            choice = int(input("""
===== STUDENT DATABASE =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

Choose: """))

            if 1 <= choice <= 6:
                return choice

            print("Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """Run the Student Database application."""

    connection, cursor = connect_database()

    create_table(connection, cursor)

    while True:
        choice = main_menu()

        if choice == 1:
            add_student(connection, cursor)

        elif choice == 2:
            view_students(connection, cursor)

        elif choice == 3:
            search_student(connection, cursor)

        elif choice == 4:
            update_student(connection, cursor)

        elif choice == 5:
            delete_student(connection, cursor)

        elif choice == 6:
            print("Goodbye!")
            break

    connection.close()


if __name__ == "__main__":
    main()