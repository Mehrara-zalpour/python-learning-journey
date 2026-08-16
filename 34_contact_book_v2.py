"""
Project 34

Contact Book v2

A command-line contact management application built with Python.

Features:

- Add contacts
- View contacts
- Search contacts by name, phone, email, or category
- Update contacts by ID
- Delete contacts by ID
- Store contacts in a JSON file
- Validate user input

Concepts practiced:

- Functions
- Lists and dictionaries
- JSON
- File handling
- os module
- Loops
- Conditional statements
- Exception handling
- Input validation
- String processing
- Searching
- Adding, updating, and deleting data
"""

import json
import os


FILE_NAME = "contacts.json"


def main_menu():

    while True:

        try:
            choice = int(input("""
====== CONTACT BOOK ======

1. Add Contact
2. View Contacts
3. Search Contacts
4. Update Contact
5. Delete Contact
6. Exit

Choose: """))

            if 1 <= choice <= 6:
                return choice

            print("Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def load_contacts():

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return []


def save_contacts(contacts):

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):

    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    category = input("Category: ").strip()

    contact_id = len(contacts) + 1

    contact = {
        "id": contact_id,
        "name": name,
        "phone": phone,
        "email": email,
        "category": category
    }

    contacts.append(contact)

    save_contacts(contacts)

    print("Contact added successfully.")


def view_contacts():

    contacts = load_contacts()

    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:

        print("\n--------------------")
        print(f"ID: {contact['id']}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"Category: {contact['category']}")
        print("--------------------")


def search_contacts(contacts):

    while True:

        keyword = input("Enter search: ").strip().lower()

        if not keyword:
            print("Search box cannot be empty.")
            continue

        break

    results = []

    for contact in contacts:

        if (
            keyword in contact["name"].lower()
            or keyword in contact["phone"].lower()
            or keyword in contact["email"].lower()
            or keyword in contact["category"].lower()
        ):
            results.append(contact)

    return results


def update_contact(contacts):

    while True:

        try:
            contact_id = input("Enter contact ID: ").strip()

            if not contact_id:
                print("Contact ID cannot be empty.")
                continue

            contact_id = int(contact_id)

            if contact_id > 0:
                break

            print("Contact ID must be greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    for contact in contacts:

        if contact["id"] == contact_id:

            new_name = input(
                f"Name ({contact['name']}): "
            ).strip()

            if new_name:
                contact["name"] = new_name

            new_phone = input(
                f"Phone ({contact['phone']}): "
            ).strip()

            if new_phone:
                contact["phone"] = new_phone

            new_email = input(
                f"Email ({contact['email']}): "
            ).strip()

            if new_email:
                contact["email"] = new_email

            new_category = input(
                f"Category ({contact['category']}): "
            ).strip()

            if new_category:
                contact["category"] = new_category

            save_contacts(contacts)

            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact(contacts):

    while True:

        try:
            contact_id = input("Enter contact ID: ").strip()

            if not contact_id:
                print("Contact ID cannot be empty.")
                continue

            contact_id = int(contact_id)

            if contact_id > 0:
                break

            print("Contact ID must be greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    for contact in contacts:

        if contact["id"] == contact_id:

            contacts.remove(contact)

            save_contacts(contacts)

            print("Contact deleted successfully.")
            return

    print("Contact not found.")


def main():

    contacts = load_contacts()

    while True:

        choice = main_menu()

        if choice == 1:
            add_contact(contacts)

        elif choice == 2:
            view_contacts()

        elif choice == 3:

            results = search_contacts(contacts)

            print("\n====== SEARCH RESULTS ======")

            if not results:
                print("No matching contacts found.")

            else:
                for contact in results:
                    print("\n--------------------")
                    print(f"ID: {contact['id']}")
                    print(f"Name: {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                    print(f"Category: {contact['category']}")
                    print("--------------------")

        elif choice == 4:
            update_contact(contacts)

        elif choice == 5:
            delete_contact(contacts)

        elif choice == 6:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()