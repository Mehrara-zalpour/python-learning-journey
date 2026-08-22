"""
Project 38 - Habit Tracker

A command-line habit tracking application built with Python and SQLite.

Features:
- Add new habits
- View all habits
- Log completed habits with duration
- View habit history
- Update habit information
- Deactivate habits without deleting their history
- View habit statistics

Database:
- SQLite
- Two related tables: habits and habit_logs
- Foreign key relationship between the tables

Concepts practiced:
- Functions
- SQLite and sqlite3
- Multiple related tables
- Primary keys and foreign keys
- SQL JOIN
- INSERT
- SELECT
- UPDATE
- GROUP BY
- COUNT()
- SUM()
- AVG()
- datetime
- Input validation
- Exception handling
- Soft delete
"""

import sqlite3
from datetime import datetime


def connect_database():
    """Connect to the SQLite database."""

    connection = sqlite3.connect("habit.db")
    connection.execute("PRAGMA foreign_keys = ON")

    cursor = connection.cursor()

    return connection, cursor


def create_tables(connection, cursor):
    """Create database tables if they do not already exist."""

    habits_sql = """
    CREATE TABLE IF NOT EXISTS habits (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        active INTEGER NOT NULL
    )
    """

    habit_logs_sql = """
    CREATE TABLE IF NOT EXISTS habit_logs (
        id INTEGER PRIMARY KEY,
        habit_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        duration INTEGER NOT NULL,
        FOREIGN KEY (habit_id) REFERENCES habits(id)
    )
    """

    cursor.execute(habits_sql)
    cursor.execute(habit_logs_sql)

    connection.commit()


def add_habit(connection, cursor):
    """Add a new habit to the database."""

    print("\n===== ADD HABIT =====")

    while True:
        name = input("Habit name: ").strip()

        if not name:
            print("Habit name cannot be empty.")
            continue

        break

    while True:
        description = input("Description: ").strip()

        if not description:
            print("Description cannot be empty.")
            continue

        break

    sql = """
    INSERT INTO habits (name, description, active)
    VALUES (?, ?, ?)
    """

    cursor.execute(sql, (name, description, 1))
    connection.commit()

    print("Habit added successfully.")


def view_habits(connection, cursor):
    """Display all habits."""

    sql = "SELECT * FROM habits"

    cursor.execute(sql)
    habits = cursor.fetchall()

    if not habits:
        print("No habits found.")
        return

    print("\n===== HABITS =====")

    for habit in habits:
        status = "Active" if habit[3] == 1 else "Inactive"

        print(
            f"ID: {habit[0]} | "
            f"Name: {habit[1]} | "
            f"Description: {habit[2]} | "
            f"Status: {status}"
        )


def log_habit(connection, cursor):
    """Log the completion of an active habit."""

    sql = "SELECT * FROM habits WHERE active = 1"

    cursor.execute(sql)
    habits = cursor.fetchall()

    if not habits:
        print("No active habits found.")
        return

    print("\n===== LOG HABIT =====")

    for number, habit in enumerate(habits, start=1):
        print(f"{number}. {habit[1]}")

    while True:
        try:
            choice = int(input("Choose a habit: "))

            if choice < 1 or choice > len(habits):
                print(
                    f"Please enter a number between 1 and {len(habits)}."
                )
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    habit_id = habits[choice - 1][0]

    while True:
        try:
            duration = int(input("Duration (minutes): "))

            if duration <= 0:
                print("Please enter a duration greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    today = datetime.now().date()

    insert_sql = """
    INSERT INTO habit_logs (habit_id, date, duration)
    VALUES (?, ?, ?)
    """

    cursor.execute(insert_sql, (habit_id, today, duration))
    connection.commit()

    print("Habit logged successfully.")


def view_habit_logs(connection, cursor):
    """Display all habit logs."""

    sql = """
    SELECT
        habits.name,
        habit_logs.date,
        habit_logs.duration
    FROM habit_logs
    JOIN habits ON habit_logs.habit_id = habits.id
    """

    cursor.execute(sql)
    logs = cursor.fetchall()

    if not logs:
        print("No habit logs found.")
        return

    print("\n===== HABIT LOGS =====")

    for log in logs:
        print(
            f"Habit: {log[0]} | "
            f"Date: {log[1]} | "
            f"Duration: {log[2]} minutes"
        )


def update_habit(connection, cursor):
    """Update an existing habit."""

    sql = "SELECT * FROM habits"

    cursor.execute(sql)
    habits = cursor.fetchall()

    if not habits:
        print("No habits found.")
        return

    print("\n===== UPDATE HABIT =====")

    for number, habit in enumerate(habits, start=1):
        status = "Active" if habit[3] == 1 else "Inactive"

        print(
            f"{number}. {habit[1]} | "
            f"Status: {status}"
        )

    while True:
        try:
            choice = int(input("Choose a habit: "))

            if choice < 1 or choice > len(habits):
                print(
                    f"Please enter a number between 1 and {len(habits)}."
                )
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    habit_id = habits[choice - 1][0]

    while True:
        try:
            option = int(input("""
===== UPDATE =====

1. Change name
2. Change description
3. Change status
4. Cancel

Choose an option: """))

            if option == 1:
                name = input("New name: ").strip()

                if not name:
                    print("Name cannot be empty.")
                    continue

                update_sql = """
                UPDATE habits
                SET name = ?
                WHERE id = ?
                """

                cursor.execute(update_sql, (name, habit_id))
                connection.commit()

                print("Habit name updated successfully.")
                break

            elif option == 2:
                description = input("New description: ").strip()

                if not description:
                    print("Description cannot be empty.")
                    continue

                update_sql = """
                UPDATE habits
                SET description = ?
                WHERE id = ?
                """

                cursor.execute(update_sql, (description, habit_id))
                connection.commit()

                print("Habit description updated successfully.")
                break

            elif option == 3:
                while True:
                    try:
                        status_choice = int(
                            input("Choose status (1=Active, 2=Inactive): ")
                        )

                        if status_choice not in (1, 2):
                            print("Please enter 1 or 2.")
                            continue

                        break

                    except ValueError:
                        print("Invalid input. Please enter 1 or 2.")

                active = 1 if status_choice == 1 else 0

                update_sql = """
                UPDATE habits
                SET active = ?
                WHERE id = ?
                """

                cursor.execute(update_sql, (active, habit_id))
                connection.commit()

                print("Habit status updated successfully.")
                break

            elif option == 4:
                print("Update cancelled.")
                break

            else:
                print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def delete_habit(connection, cursor):
    """Deactivate a habit without deleting its history."""

    sql = "SELECT * FROM habits"

    cursor.execute(sql)
    habits = cursor.fetchall()

    if not habits:
        print("No habits found.")
        return

    print("\n===== DELETE HABIT =====")

    for number, habit in enumerate(habits, start=1):
        status = "Active" if habit[3] == 1 else "Inactive"

        print(
            f"{number}. {habit[1]} | "
            f"Status: {status}"
        )

    while True:
        try:
            choice = int(input("Choose a habit: "))

            if choice < 1 or choice > len(habits):
                print(
                    f"Please enter a number between 1 and {len(habits)}."
                )
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    habit_id = habits[choice - 1][0]
    habit_name = habits[choice - 1][1]

    while True:
        confirmation = input(
            f"Are you sure you want to deactivate "
            f"'{habit_name}'? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            break

        if confirmation == "n":
            print("Deletion cancelled.")
            return

        print("Please enter 'y' or 'n'.")

    update_sql = """
    UPDATE habits
    SET active = 0
    WHERE id = ?
    """

    cursor.execute(update_sql, (habit_id,))
    connection.commit()

    print("Habit deactivated successfully.")


def habit_statistics(connection, cursor):
    """Display statistics for each habit."""

    sql = """
    SELECT
        habits.name,
        COUNT(habit_logs.id),
        SUM(habit_logs.duration),
        AVG(habit_logs.duration)
    FROM habit_logs
    JOIN habits ON habit_logs.habit_id = habits.id
    GROUP BY habits.id, habits.name
    """

    cursor.execute(sql)
    statistics = cursor.fetchall()

    if not statistics:
        print("No habit logs found.")
        return

    print("\n===== HABIT STATISTICS =====")

    for statistic in statistics:
        name = statistic[0]
        sessions = statistic[1]
        total_minutes = statistic[2]
        average_duration = statistic[3]

        print(
            f"Habit: {name} | "
            f"Sessions: {sessions} | "
            f"Total: {total_minutes} minutes | "
            f"Average: {average_duration:.1f} minutes"
        )


def main_menu(connection, cursor):
    """Display the main menu and handle user choices."""

    while True:
        print("""
===== HABIT TRACKER =====

1. Add Habit
2. View Habits
3. Log Habit
4. View Habit Logs
5. Update Habit
6. Delete Habit
7. Habit Statistics
8. Exit
""")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                add_habit(connection, cursor)

            elif choice == 2:
                view_habits(connection, cursor)

            elif choice == 3:
                log_habit(connection, cursor)

            elif choice == 4:
                view_habit_logs(connection, cursor)

            elif choice == 5:
                update_habit(connection, cursor)

            elif choice == 6:
                delete_habit(connection, cursor)

            elif choice == 7:
                habit_statistics(connection, cursor)

            elif choice == 8:
                print("Goodbye! 👋")
                break

            else:
                print("Please enter a number between 1 and 8.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """Run the Habit Tracker application."""

    connection, cursor = connect_database()

    try:
        create_tables(connection, cursor)
        main_menu(connection, cursor)

    finally:
        connection.close()


if __name__ == "__main__":
    main()