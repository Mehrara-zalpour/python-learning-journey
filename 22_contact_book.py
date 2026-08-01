"""
Project 22: Contact Book

Description:
A simple command-line Contact Book application.

Features:
- Show all contacts
- Add a new contact
- Search for a contact
- Delete a contact

Concepts Practiced:
- Functions
- File Handling
- readlines()
- writelines()
- String Methods
- split()
- strip()
- Loops
- enumerate()
- Input Validation
- CRUD Basics

Author:
Mehrara
"""

def main_menu():
    while True:
        try:
            choice = int(input("""

====== CONTACT BOOK ======

1. Show Contacts
2. Add Contact
3. Delete Contact
4. Search Contact
5. Exit

Choose: """))

            if 1 <= choice <= 5:
                return choice

            print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def show_contacts():
    print("\n===== Your Contacts =====")

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    if not contacts:
        print("No contacts found.")
        return

    for line in contacts:

        if "," not in line:
            continue

        name, phone = line.strip().split(",")

        print(f"{name}: {phone}")


def add_contact():
    print("\n===== Add Contact =====")

    name = input("Enter name: ").strip().lower()
    phone = input("Enter phone number: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty.")
        return

    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")

    print("Contact added successfully.")


def search_contact(name_search):
    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    if not contacts:
        return None

    for index, line in enumerate(contacts):

        if "," not in line:
            continue

        name, phone = line.strip().split(",")

        if name.lower() == name_search.lower():
            return index, line

    return None


def search():
    print("\n===== Search Contact =====")

    name = input("Enter name: ").strip()

    result = search_contact(name)

    if result is None:
        print("No contact found.")
        return

    _, line = result

    name, phone = line.strip().split(",")

    print(f"{name}: {phone}")


def delete_contact():
    print("\n===== Delete Contact =====")

    name = input("Enter name: ").strip()

    result = search_contact(name)

    if result is None:
        print("No contact found.")
        return

    index, _ = result

    with open("contacts.txt", "r") as file:
        contacts = file.readlines()

    del contacts[index]

    with open("contacts.txt", "w") as file:
        file.writelines(contacts)

    print("Contact deleted successfully.")


def main():
    while True:

        choice = main_menu()

        if choice == 1:
            show_contacts()

        elif choice == 2:
            add_contact()

        elif choice == 3:
            delete_contact()

        elif choice == 4:
            search()

        elif choice == 5:
            print("Goodbye!")
            break


main()