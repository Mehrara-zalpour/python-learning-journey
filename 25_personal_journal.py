"""
Project 25: Personal Journal (JSON)

Description:
A command-line application for managing personal notes.
Users can create, view, search, and delete notes.
All notes are stored permanently in a JSON file.

Features:
- View all notes
- Add a new note
- Search notes by title
- Delete notes
- Store data in JSON format

Concepts Practiced:
- JSON Handling (json.load, json.dump)
- Reading and Writing JSON Files
- Dictionaries
- Nested Dictionaries
- CRUD Operations
- Functions
- Loops
- Exception Handling
- Input Validation
"""
import json


FILE_NAME = "journal.json"


def main_menu():
    while True:
        try:
            choice = int(input("""
====== PERSONAL JOURNAL ======

1. View All Notes
2. Add Note
3. Search Note
4. Delete Note
5. Exit

Choose an option: """))

            if 1 <= choice <= 5:
                return choice

            print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def load_journal():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_journal(journal):
    with open(FILE_NAME, "w") as file:
        json.dump(journal, file, indent=4)


def add_note():
    print("\n===== Add Note =====")

    title = input("Enter note title: ")
    text = input("Enter note text: ")
    category = input("Enter note category: ")

    if not title or not text or not category:
        print("Title, text and category cannot be empty.")
        return

    journal = load_journal()

    if title in journal:
        print("This title already exists.")
        return

    journal[title] = {
        "text": text,
        "category": category
    }

    save_journal(journal)

    print("Note added successfully.")


def view_notes():
    print("\n===== Your Notes =====")

    journal = load_journal()

    if not journal:
        print("No notes found.")
        return

    for title, note in journal.items():
        print("\n--------------------")
        print(f"Title: {title}")
        print(f"Text: {note['text']}")
        print(f"Category: {note['category']}")

    print("--------------------")


def search_note():
    print("\n===== Search Note =====")

    title = input("Enter note title: ")

    if not title:
        print("Title cannot be empty.")
        return

    journal = load_journal()

    if title in journal:
        print("\n--------------------")
        print(f"Title: {title}")
        print(f"Text: {journal[title]['text']}")
        print(f"Category: {journal[title]['category']}")
        print("--------------------")

    else:
        print("Note not found.")


def delete_note():
    print("\n===== Delete Note =====")

    title = input("Enter note title: ")

    if not title:
        print("Title cannot be empty.")
        return

    journal = load_journal()

    if title in journal:
        del journal[title]

        save_journal(journal)

        print("Note deleted successfully.")

    else:
        print("Note not found.")


def main():

    while True:

        choice = main_menu()

        if choice == 1:
            view_notes()

        elif choice == 2:
            add_note()

        elif choice == 3:
            search_note()

        elif choice == 4:
            delete_note()

        elif choice == 5:
            print("Goodbye!")
            break


main()