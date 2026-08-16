"""
Project 35

Expense Tracker Pro

A command-line expense tracking application built with Python.

Features:

- Add expenses
- View expenses
- Search expenses
- Filter expenses by category
- Calculate total expenses
- Update expenses
- Delete expenses
- Display expense charts

Concepts practiced:

- Functions
- Lists and dictionaries
- JSON
- File handling
- os module
- datetime module
- Loops
- Conditional statements
- Exception handling
- Input validation
- Searching and filtering
- Data analysis
- matplotlib
- Data visualization
"""

import json
import os
from datetime import datetime

import matplotlib.pyplot as plt


FILE_NAME = "expenses.json"


def main_menu():

    while True:

        try:
            choice = int(input("""
====== EXPENSE TRACKER ======

1. Add Expense
2. View Expenses
3. Search Expenses
4. Filter Expenses by Category
5. Calculate Total Expenses
6. Update Expense
7. Delete Expense
8. Display Expense Chart
9. Exit

Choose: """))

            if 1 <= choice <= 9:
                return choice

            print("Please enter a number between 1 and 9.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def load_expenses():

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)

    except json.JSONDecodeError:
        print("Invalid JSON file.")
        return []


def save_expenses(expenses):

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):

    while True:

        title = input("Enter title: ").strip()

        if not title:
            print("Title cannot be empty.")
            continue

        break

    while True:

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid amount.")

    while True:

        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty.")
            continue

        break

    while True:

        description = input("Enter description: ").strip()

        if not description:
            print("Description cannot be empty.")
            continue

        break

    expense_id = len(expenses) + 1

    expense = {
        "id": expense_id,
        "title": title,
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description
    }

    expenses.append(expense)

    save_expenses(expenses)

    print("Expense added successfully.")


def view_expenses():

    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:

        print("\n--------------------")
        print(f"ID: {expense['id']}")
        print(f"Title: {expense['title']}")
        print(f"Amount: {expense['amount']}")
        print(f"Category: {expense['category']}")
        print(f"Date: {expense['date']}")
        print(f"Description: {expense['description']}")
        print("--------------------")


def search_expenses(expenses):

    while True:

        keyword = input("Enter search: ").strip().lower()

        if not keyword:
            print("Search box cannot be empty.")
            continue

        break

    results = []

    for expense in expenses:

        if (
            keyword in expense["title"].lower()
            or keyword in str(expense["amount"])
            or keyword in expense["category"].lower()
            or keyword in expense["date"]
            or keyword in expense["description"].lower()
        ):
            results.append(expense)

    return results


def filter_by_category(expenses):

    while True:

        category = input("Enter category: ").strip().lower()

        if not category:
            print("Category cannot be empty.")
            continue

        break

    results = []

    for expense in expenses:

        if expense["category"].lower() == category:
            results.append(expense)

    return results


def calculate_total(expenses):

    total_expenses = 0

    for expense in expenses:
        total_expenses += expense["amount"]

    return total_expenses


def update_expense(expenses):

    while True:

        try:
            expense_id = input("Enter Expense ID: ").strip()

            if not expense_id:
                print("Expense ID cannot be empty.")
                continue

            expense_id = int(expense_id)

            if expense_id <= 0:
                print("Expense ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    for expense in expenses:

        if expense["id"] == expense_id:

            new_title = input(
                f"Title ({expense['title']}): "
            ).strip()

            if new_title:
                expense["title"] = new_title

            while True:

                new_amount = input(
                    f"Amount ({expense['amount']}): "
                ).strip()

                if not new_amount:
                    break

                try:
                    new_amount = float(new_amount)

                    if new_amount <= 0:
                        print("Amount must be greater than 0.")
                        continue

                    expense["amount"] = new_amount
                    break

                except ValueError:
                    print("Invalid amount. Please enter a number.")

            new_category = input(
                f"Category ({expense['category']}): "
            ).strip()

            if new_category:
                expense["category"] = new_category

            new_description = input(
                f"Description ({expense['description']}): "
            ).strip()

            if new_description:
                expense["description"] = new_description

            save_expenses(expenses)

            print("Expense updated successfully.")
            return

    print("Expense not found.")


def delete_expense(expenses):

    while True:

        try:
            expense_id = input("Enter Expense ID: ").strip()

            if not expense_id:
                print("Expense ID cannot be empty.")
                continue

            expense_id = int(expense_id)

            if expense_id <= 0:
                print("Expense ID must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    for expense in expenses:

        if expense["id"] == expense_id:

            expenses.remove(expense)

            save_expenses(expenses)

            print("Expense deleted successfully.")
            return

    print("Expense not found.")


def show_chart(expenses):

    if not expenses:
        print("No expenses available to display.")
        return

    category_totals = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category not in category_totals:
            category_totals[category] = 0

        category_totals[category] += amount

    categories = list(category_totals.keys())
    amounts = list(category_totals.values())

    plt.bar(categories, amounts)

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.tight_layout()
    plt.show()


def main():

    expenses = load_expenses()

    while True:

        choice = main_menu()

        if choice == 1:

            add_expense(expenses)

        elif choice == 2:

            view_expenses()

        elif choice == 3:

            results = search_expenses(expenses)

            print("\n====== SEARCH RESULTS ======")

            if not results:
                print("No matching expenses found.")
            else:
                for expense in results:
                    print(
                        f"{expense['id']} | "
                        f"{expense['title']} | "
                        f"{expense['amount']} | "
                        f"{expense['category']} | "
                        f"{expense['date']}"
                    )

        elif choice == 4:

            results = filter_by_category(expenses)

            print("\n====== FILTER RESULTS ======")

            if not results:
                print("No expenses found in this category.")
            else:
                for expense in results:
                    print(
                        f"{expense['id']} | "
                        f"{expense['title']} | "
                        f"{expense['amount']} | "
                        f"{expense['category']} | "
                        f"{expense['date']}"
                    )

        elif choice == 5:

            total = calculate_total(expenses)

            print(f"\nTotal Expenses: {total:.2f}")

        elif choice == 6:

            update_expense(expenses)

        elif choice == 7:

            delete_expense(expenses)

        elif choice == 8:

            show_chart(expenses)

        elif choice == 9:

            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
