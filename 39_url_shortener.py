"""
Project 39 - URL Shortener

A command-line URL shortening application built with Python and SQLite.

Features:
- Shorten URLs using SHA-256 hashing
- Generate a unique short code
- Store original URLs and short codes
- View all shortened URLs
- Find an original URL using its short code
- Delete shortened URLs

Database:
- SQLite
- URLs table
- Primary key
- Unique short codes

Concepts practiced:
- Functions
- SQLite and sqlite3
- Database CRUD operations
- INSERT
- SELECT
- DELETE
- WHERE
- fetchone()
- fetchall()
- SHA-256 hashing
- hashlib
- String encoding
- datetime
- Input validation
- Exception handling
"""

import sqlite3
import hashlib
from datetime import datetime


def connect_database():
    """Connect to the SQLite database."""

    connection = sqlite3.connect("url_shortener.db")
    cursor = connection.cursor()

    return connection, cursor


def create_table(connection, cursor):
    """Create the URLs table if it does not exist."""

    sql = """
    CREATE TABLE IF NOT EXISTS urls (
        id INTEGER PRIMARY KEY,
        original_url TEXT NOT NULL,
        short_code TEXT NOT NULL UNIQUE,
        created_at TEXT NOT NULL
    )
    """

    cursor.execute(sql)
    connection.commit()


def shorten_url(connection, cursor):
    """Create a short code for a URL and save it in the database."""

    print("\n===== SHORTEN URL =====")

    while True:
        original_url = input("Enter URL: ").strip()

        if not original_url:
            print("URL cannot be empty.")
            continue

        break

    hash_object = hashlib.sha256(original_url.encode())
    hash_value = hash_object.hexdigest()

    short_code = hash_value[:8]
    created_at = datetime.now()

    sql = """
    INSERT INTO urls (original_url, short_code, created_at)
    VALUES (?, ?, ?)
    """

    cursor.execute(
        sql,
        (original_url, short_code, created_at)
    )

    connection.commit()

    print(f"Short code: {short_code}")


def view_urls(connection, cursor):
    """Display all shortened URLs."""

    sql = "SELECT * FROM urls"

    cursor.execute(sql)
    urls = cursor.fetchall()

    if not urls:
        print("No URLs found.")
        return

    print("\n===== URLS =====")

    for url in urls:
        print(
            f"ID: {url[0]} | "
            f"Original URL: {url[1]} | "
            f"Short Code: {url[2]} | "
            f"Created At: {url[3]}"
        )


def find_url(connection, cursor):
    """Find the original URL using its short code."""

    print("\n===== FIND URL =====")

    while True:
        short_code = input("Enter short code: ").strip()

        if not short_code:
            print("Short code cannot be empty.")
            continue

        break

    sql = """
    SELECT original_url
    FROM urls
    WHERE short_code = ?
    """

    cursor.execute(sql, (short_code,))
    result = cursor.fetchone()

    if not result:
        print("Short code not found.")
        return

    print(f"Original URL: {result[0]}")


def delete_url(connection, cursor):
    """Delete a shortened URL from the database."""

    sql = "SELECT * FROM urls"

    cursor.execute(sql)
    urls = cursor.fetchall()

    if not urls:
        print("No URLs found.")
        return

    print("\n===== DELETE URL =====")

    for url in urls:
        print(
            f"ID: {url[0]} | "
            f"Original URL: {url[1]} | "
            f"Short Code: {url[2]} | "
            f"Created At: {url[3]}"
        )

    while True:
        try:
            url_id = int(input("Enter URL ID: "))

            if url_id <= 0:
                print("ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    check_sql = """
    SELECT original_url
    FROM urls
    WHERE id = ?
    """

    cursor.execute(check_sql, (url_id,))
    url = cursor.fetchone()

    if not url:
        print("URL ID not found.")
        return

    while True:
        confirmation = input(
            f"Are you sure you want to delete '{url[0]}'? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            break

        if confirmation == "n":
            print("Deletion cancelled.")
            return

        print("Please enter 'y' or 'n'.")

    delete_sql = """
    DELETE FROM urls
    WHERE id = ?
    """

    cursor.execute(delete_sql, (url_id,))
    connection.commit()

    print("URL deleted successfully.")


def main_menu(connection, cursor):
    """Display the main menu and handle user choices."""

    while True:
        print("""
===== URL SHORTENER =====

1. Shorten URL
2. View URLs
3. Find URL
4. Delete URL
5. Exit
""")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                shorten_url(connection, cursor)

            elif choice == 2:
                view_urls(connection, cursor)

            elif choice == 3:
                find_url(connection, cursor)

            elif choice == 4:
                delete_url(connection, cursor)

            elif choice == 5:
                print("Goodbye! 👋")
                break

            else:
                print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """Run the URL Shortener application."""

    connection, cursor = connect_database()

    try:
        create_table(connection, cursor)
        main_menu(connection, cursor)

    finally:
        connection.close()


if __name__ == "__main__":
    main()