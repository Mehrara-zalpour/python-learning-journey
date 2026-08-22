"""
Project 37

Library Database

A command-line library management application built with
Python and SQLite.

Features:
- Add books
- Add library members
- View books
- View members
- Borrow books
- Return books
- Search books
- Store data permanently in SQLite

Concepts practiced:
- SQLite
- sqlite3
- Multiple tables
- Primary Keys
- Foreign Keys
- SQL relationships
- CRUD operations
- INSERT
- SELECT
- UPDATE
- DELETE
- WHERE
- AND
- IS NULL
- JOIN
- Parameterized queries
- fetchone()
- fetchall()
- commit()
- datetime
- Exception handling
- Input validation
"""


import sqlite3
from datetime import datetime


def connect_database():
    """Connect to the SQLite database and enable foreign keys."""

    connection = sqlite3.connect("library.db")

    connection.execute("PRAGMA foreign_keys = ON")

    cursor = connection.cursor()

    return connection, cursor


def create_tables(connection, cursor):
    """Create all database tables if they do not already exist."""

    books = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    )
    """

    members = """
    CREATE TABLE IF NOT EXISTS members (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT
    )
    """

    loans = """
    CREATE TABLE IF NOT EXISTS loans (
        id INTEGER PRIMARY KEY,
        book_id INTEGER NOT NULL,
        member_id INTEGER NOT NULL,
        loan_date TEXT NOT NULL,
        return_date TEXT,
        FOREIGN KEY (book_id) REFERENCES books(id),
        FOREIGN KEY (member_id) REFERENCES members(id)
    )
    """

    cursor.execute(books)
    cursor.execute(members)
    cursor.execute(loans)

    connection.commit()


def add_book(connection, cursor):
    """Add a new book to the database."""

    while True:
        title = input("Enter Book Title: ").strip()

        if not title:
            print("Book Title cannot be empty.")
            continue

        break

    while True:
        author = input("Enter Author: ").strip()

        if not author:
            print("Author cannot be empty.")
            continue

        break

    while True:
        try:
            year = int(input("Enter Publication Year: "))

            if year <= 0:
                print("Year must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid year. Please enter a number.")

    sql = """
    INSERT INTO books (title, author, year)
    VALUES (?, ?, ?)
    """

    cursor.execute(sql, (title, author, year))
    connection.commit()

    print("Book added successfully.")


def add_member(connection, cursor):
    """Add a new library member to the database."""

    while True:
        name = input("Enter Member Name: ").strip()

        if not name:
            print("Member name cannot be empty.")
            continue

        break

    while True:
        phone = input("Enter Phone Number: ").strip()

        if not phone:
            print("Phone number cannot be empty.")
            continue

        break

    sql = """
    INSERT INTO members (name, phone)
    VALUES (?, ?)
    """

    cursor.execute(sql, (name, phone))
    connection.commit()

    print("Member added successfully.")


def add_loan(connection, cursor):
    """Borrow a book for a library member."""

    while True:
        try:
            book_id = int(input("Enter Book ID: "))

            if book_id <= 0:
                print("Book ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    sql = "SELECT * FROM books WHERE id = ?"

    cursor.execute(sql, (book_id,))

    book = cursor.fetchone()

    if not book:
        print("Book not found.")
        return

    loan = """
    SELECT * FROM loans
    WHERE book_id = ?
    AND return_date IS NULL
    """

    cursor.execute(loan, (book_id,))

    existing_loan = cursor.fetchone()

    if existing_loan:
        print("Book is already borrowed.")
        return

    while True:
        try:
            member_id = int(input("Enter Member ID: "))

            if member_id <= 0:
                print("Member ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    sql = "SELECT * FROM members WHERE id = ?"

    cursor.execute(sql, (member_id,))

    member = cursor.fetchone()

    if not member:
        print("Member not found.")
        return

    loan_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = """
    INSERT INTO loans (book_id, member_id, loan_date)
    VALUES (?, ?, ?)
    """

    cursor.execute(sql, (book_id, member_id, loan_date))
    connection.commit()

    print("Book borrowed successfully.")


def view_books(connection, cursor):
    """Display all books."""

    sql = "SELECT * FROM books"

    cursor.execute(sql)

    books = cursor.fetchall()

    if not books:
        print("No books found.")
        return

    print("\n===== BOOKS =====")

    for book in books:
        print(
            f"ID: {book[0]} | "
            f"Title: {book[1]} | "
            f"Author: {book[2]} | "
            f"Year: {book[3]}"
        )


def view_members(connection, cursor):
    """Display all library members."""

    sql = "SELECT * FROM members"

    cursor.execute(sql)

    members = cursor.fetchall()

    if not members:
        print("No members found.")
        return

    print("\n===== MEMBERS =====")

    for member in members:
        print(
            f"ID: {member[0]} | "
            f"Name: {member[1]} | "
            f"Phone: {member[2]}"
        )


def view_loans(connection, cursor):
    """Display all current and previous loans."""

    sql = """
    SELECT
        loans.id,
        books.title,
        members.name,
        loans.loan_date,
        loans.return_date
    FROM loans
    JOIN books ON loans.book_id = books.id
    JOIN members ON loans.member_id = members.id
    """

    cursor.execute(sql)

    loans = cursor.fetchall()

    if not loans:
        print("No loans found.")
        return

    print("\n===== LOANS =====")

    for loan in loans:
        print(
            f"Loan ID: {loan[0]} | "
            f"Book: {loan[1]} | "
            f"Member: {loan[2]} | "
            f"Loan Date: {loan[3]} | "
            f"Return Date: {loan[4]}"
        )


def search_book(connection, cursor):
    """Search for a book by ID."""

    while True:
        book_id = input("Enter Book ID: ").strip()

        if not book_id:
            print("Book ID cannot be empty.")
            continue

        try:
            book_id = int(book_id)

            if book_id <= 0:
                print("Book ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")
    
    sql = "SELECT * FROM books WHERE id = ?"

    cursor.execute(sql, (book_id,))

    book = cursor.fetchone()

    if book:
        print(
            f"ID: {book[0]} | "
            f"Title: {book[1]} | "
            f"Author: {book[2]} | "
            f"Year: {book[3]}"
        )
    else:
        print("Book not found.")


def return_book(connection, cursor):
    """Return a borrowed book."""

    while True:
        try:
            book_id = int(input("Enter Book ID: "))

            if book_id <= 0:
                print("Book ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    sql = """
    SELECT * FROM loans
    WHERE book_id = ?
    AND return_date IS NULL
    """

    cursor.execute(sql, (book_id,))

    loan = cursor.fetchone()

    if not loan:
        print("This book is not currently borrowed.")
        return

    return_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sql = """
    UPDATE loans
    SET return_date = ?
    WHERE id = ?
    """

    cursor.execute(sql, (return_date, loan[0]))
    connection.commit()

    print("Book returned successfully.")


def main_menu():
    """Display the main menu and return the user's choice."""

    while True:

        try:
            choice = int(input("""
===== LIBRARY DATABASE =====

1. Add Book
2. Add Member
3. Borrow Book
4. View Books
5. View Members
6. View Loans
7. Search Book
8. Return Book
9. Exit

Choose: """))

            if 1 <= choice <= 9:
                return choice

            print("Please enter a number between 1 and 9.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """Run the Library Database application."""

    connection, cursor = connect_database()

    create_tables(connection, cursor)

    while True:
        choice = main_menu()

        if choice == 1:
            add_book(connection, cursor)

        elif choice == 2:
            add_member(connection, cursor)

        elif choice == 3:
            add_loan(connection, cursor)

        elif choice == 4:
            view_books(connection, cursor)

        elif choice == 5:
            view_members(connection, cursor)

        elif choice == 6:
            view_loans(connection, cursor)

        elif choice == 7:
            search_book(connection, cursor)

        elif choice == 8:
            return_book(connection, cursor)

        elif choice == 9:
            print("Goodbye!")
            break

    connection.close()


if __name__ == "__main__":
    main()