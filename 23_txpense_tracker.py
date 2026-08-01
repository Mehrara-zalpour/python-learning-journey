"""
Project 23: Expense Tracker
Version: 1.0
Author: Mehrara

Description:
A simple command-line application to manage daily expenses.

Features:
- Show all expenses
- Add a new expense
- Search for an expense
- Delete an expense
- Calculate total expenses

Concepts Practiced:
- File Handling
- Dictionaries
- Functions
- Loops
- Input Validation
- Data Type Conversion
- CRUD Operations
"""

def main_menu():
    while True:
        try:
            choice = int(input("""

====== EXPENSE TRACKER ======

1. Show Expenses
2. Add Expense
3. Delete Expense
4. Show Total
5. Exit

Choose: """))

            if 1 <= choice <= 5:
                return choice

            print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def show_expenses():
    print("\n===== Your Expenses =====")

    expenses = {}

    with open("expenses.txt", "r") as file:
        for line in file:

            if "," not in line:
                continue

            key, value = line.strip().split(",")
            expenses[key] = value

    if not expenses:
        print("No expenses found.")
        return

    for key, value in expenses.items():
        print(f"{key}: {value}")


def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


def add_expenses():
    print("\n===== Add Expense =====")

    name = input("Enter name: ").strip().lower()

    if not name:
        print("Name cannot be empty.")
        return

    value = get_number("Enter value: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{name},{value}\n")

    print("Expense added successfully.")


def search_expenses(name_search):

    expenses = {}

    with open("expenses.txt", "r") as file:
        for line in file:

            if "," not in line:
                continue

            name, value = line.strip().split(",")
            expenses[name] = value

    if not expenses:
        print("No expenses found.")
        return None

    for name, value in expenses.items():
        if name.lower() == name_search.lower():
            return name, value

    return None


def search_expense():
    print("\n===== Search Expenses =====")

    name = input("Enter name: ").strip()

    result = search_expenses(name)

    if result is None:
        print("No expenses found.")
        return

    name, value = result
    print(f"{name}: {value}")


def delete_expenses():
    print("\n===== Delete Expense =====")

    name = input("Enter name: ").strip().lower()

    expenses = {}

    with open("expenses.txt", "r") as file:
        for line in file:

            if "," not in line:
                continue

            key, value = line.strip().split(",")
            expenses[key] = value

    if not expenses:
        print("No expenses found.")
        return

    if name not in expenses:
        print("Expense not found.")
        return

    del expenses[name]

    with open("expenses.txt", "w") as file:
        for key, value in expenses.items():
            file.write(f"{key},{value}\n")

    print("Expense deleted successfully.")


def show_total():

    print("===== Total Expenses =====")

    expenses = {}

    with open("expenses.txt", "r") as file:

        for line in file:

            if "," not in line:
                continue

            key, value = line.strip().split(",")
            expenses[key] = value

    if not expenses:
            print("No expenses found.")
            return

    counter = 0
    for name, value in expenses.items():
        counter += int(value)

    print(f"Total: {counter}")
    return

        


def main():
    while True:

        choice = main_menu()

        if choice == 1:
            show_expenses()

        elif choice == 2:
            add_expenses()

        elif choice == 3:
            delete_expenses()

        elif choice == 4:
            show_total()

        elif choice == 5:
            print("Goodbye!")
            break


main()
