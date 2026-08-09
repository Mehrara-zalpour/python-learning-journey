"""
Project 30

Notes Manager

A command-line notes management application built with Python.

Features:

* Create, view, search, and delete notes
* Organize notes into folders
* Store notes as text files

Concepts practiced:

* Functions
* File handling
* os module
* Directories and file paths
* Reading and writing files
* Input validation
* Error handling
* Searching text

Libraries:

* os
  """

import os

os.makedirs("notes", exist_ok=True)


def main_menu():

    while True:

        choose_input = input("""

===== NOTES MANAGER =====

1. Create Note
2. View Notes
3. Search Notes
4. Delete Note
5. Exit

choose:   """)
        if not choose_input:
            print("Choose cannot be empty.")
            continue
        try:

            choose = int(choose_input)

            if 1 <= choose <= 5:
                return choose
            print("please enter a number between 1 - 5.")

        except ValueError:
            print("Invalid Input. please enter a number.")


def create_note():
    category = input("Enter category: ").strip()
    title = input("Enter note title: ").strip()
    text = input("Enter note text: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    if not title:
        print("Title cannot be empty.")
        return

    if not text:
        print("Note text cannot be empty.")
        return

    category_path = os.path.join("notes", category)

    if not os.path.exists(category_path):
        os.makedirs(category_path)

    file_path = os.path.join(category_path, f"{title}.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

    print("Note created successfully.")


def view_notes():

    categories = os.listdir("notes")

    if not categories:
        print("No notes found.")
        return

    for category in categories:
        category_path = os.path.join("notes", category)

        if not os.path.isdir(category_path):
            continue

        print(f"\n===== {category.upper()} =====")

        files = os.listdir(category_path)

        if not files:
            print("No notes in this category.")
            continue

        for file_name in files:
            file_path = os.path.join(category_path, file_name)

            if not os.path.isfile(file_path):
                continue

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            print(f"\n{file_name}")
            print(content)


def search_notes():
    search_term = input("Enter search term: ").strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    found = False

    categories = os.listdir("notes")

    for category in categories:
        category_path = os.path.join("notes", category)

        if not os.path.isdir(category_path):
            continue

        files = os.listdir(category_path)

        for file_name in files:
            file_path = os.path.join(category_path, file_name)

            if not os.path.isfile(file_path):
                continue

            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            if search_term.lower() in content.lower():
                print(f"\nFound in: {category}/{file_name}")
                print(content)
                found = True

    if not found:
        print("No matching notes found.")


def delete_note():
    category = input("Enter category: ").strip()
    title = input("Enter note title: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    if not title:
        print("Title cannot be empty.")
        return

    file_path = os.path.join("notes", category, f"{title}.txt")

    if not os.path.exists(file_path):
        print("Note not found.")
        return

    os.remove(file_path)

    print("Note deleted successfully.")


def main():

    while True:

        choice = main_menu()

        if choice == 1:
            create_note()

        if choice == 2:
            view_notes()

        if choice == 3:
            search_notes()

        if choice == 4:
            delete_note()

        if choice == 5:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
