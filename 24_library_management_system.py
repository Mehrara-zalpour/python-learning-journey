"""
Project 24: Library Management System

Description:
A command-line application for managing a small library.

Features:
- Show all books
- Add a new book
- Search a book
- Borrow a book
- Return a book
- Delete a book

Concepts Practiced:
- File Handling
- Nested Dictionaries
- CRUD Operations
- Functions
- Loops
- Input Validation
- Data Type Conversion
"""


def main_menu():

    while True:
        try:
            choice = int(input("""

====== LIBRARY MANAGEMENT ======

1. Show Books
2. Add Book
3. Search Book
4. Borrow Book
5. Return Book
6. Delete Book
7. Exit

Choose:   """))
            if 1 <= choice <= 7:
                return choice

            print("Please enter a number between 1 and 7.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def show_books():
    print("\n===== Your Books =====")

    books = {}
    with open("books.txt", "r") as file:
        for line in file:

            if "," not in line:
                continue

            title, author, status = line.strip().split(",")
            books[title] = {
                "author": author,
                "status": status
            }

    if not books:
        print("No books found.")
        return

    for title, info in books.items():
        print(f"Title : {title}")
        print(f"Author: {info['author']}")
        print(f"Status: {info['status']}")
        print("-" * 30)


def add_book():
    print("\n===== Add Books =====")

    title = input("Enter a Title Book: ").strip().lower()
    author = input("Enter a Author Book: ").strip().lower()
    status = "Available"

    if not title or not author or not status:
        print("title, author and status cannot be empty.")
        return

    with open("books.txt", "a") as file:
        file.write(f"{title},{author},{status}\n")

    print("Book added successfully.")


def search_book():
    print("\n===== Search Book =====")

    search = input("Enter book title: ").strip().lower()

    books = {}

    with open("books.txt", "r") as file:
        for line in file:

            if "," not in line:
                continue

            title, author, status = line.strip().split(",")

            books[title] = {
                "author": author,
                "status": status
            }

    if not books:
        print("No books found.")
        return

    if search not in books:
        print("Book not found.")
        return

    print(f"Title : {search}")
    print(f"Author: {books[search]['author']}")
    print(f"Status: {books[search]['status']}")


def borrow_book():
    print("\n===== Borrow Book =====")

    borrow_name = input("Enter book title: ").strip().lower()

    if not borrow_name:
        print("Book title cannot be empty.")
        return

    books = {}

    with open("books.txt", "r") as file:
        for line in file:

            if "," not in line:
                continue

            title, author, status = line.strip().split(",")

            books[title] = {
                "author": author,
                "status": status
            }

    if not books:
        print("No books found.")
        return

    if borrow_name not in books:
        print("Book not found.")
        return

    if books[borrow_name]["status"].lower() == "borrowed":
        print("This book is already borrowed.")
        return

    books[borrow_name]["status"] = "Borrowed"

    with open("books.txt", "w") as file:
        for title, info in books.items():
            file.write(f"{title},{info['author']},{info['status']}\n")

    print("Book borrowed successfully.")


def return_book():
    print("\n===== Return Book =====")

    return_name = input("Enter book title: ").strip().lower()

    if not return_name:
        print("Book title cannot be empty.")
        return

    books = {}

    with open("books.txt", "r") as file:
        for line in file:

            if "," not in line:
                continue

            title, author, status = line.strip().split(",")

            books[title] = {
                "author": author,
                "status": status
            }

    if not books:
        print("No books found.")
        return

    if return_name not in books:
        print("Book not found.")
        return

    if books[return_name]["status"].lower() == "available":
        print("This book is already available.")
        return

    books[return_name]["status"] = "Available"

    with open("books.txt", "w") as file:
        for title, info in books.items():
            file.write(f"{title},{info['author']},{info['status']}\n")

    print("Book returned successfully.")


def delete_book():
    print("\n===== Delete Book =====")

    delete_name = input("Enter book title: ").strip().lower()

    if not delete_name:
        print("Book title cannot be empty.")
        return

    books = {}

    with open("books.txt", "r") as file:
        for line in file:

            if "," not in line:
                continue

            title, author, status = line.strip().split(",")

            books[title] = {
                "author": author,
                "status": status
            }

    if not books:
        print("No books found.")
        return

    if delete_name not in books:
        print("Book not found.")
        return

    del books[delete_name]

    with open("books.txt", "w") as file:
        for title, info in books.items():
            file.write(f"{title},{info['author']},{info['status']}\n")

    print("Book deleted successfully.")


def main():

    while True:

        choice = main_menu()

        if choice == 1:
            show_books()

        elif choice == 2:
            add_book()

        elif choice == 3:
            search_book()

        elif choice == 4:
            borrow_book()

        elif choice == 5:
            return_book()

        elif choice == 6:
            delete_book()

        elif choice == 7:
            print("Goodbye!")
            break


main()
