"""
Project 20

Mini Banking System

Description:
A simple banking system that allows the user to
view balance, deposit money, and withdraw money.

Features:
- Show balance
- Deposit money
- Withdraw money
- Input validation
- Functions
- Menu system

Author: Mehrara
Date: 2026-07-22
"""

def main_menu():
    while True:
        try:
            choice = int(input("""

===== Mini Bank =====

1. Show Balance
2. Deposit
3. Withdraw
4. Exit

Choose: """))

            if 1 <= choice <= 4:
                return choice

            print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount > 0:
                return amount

            print("Amount must be greater than zero.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def show_balance(balance):
    print(f"\nCurrent Balance: ${balance:.2f}")


def deposit(balance, amount):
    return balance + amount


def withdraw(balance, amount):
    return balance - amount


def main():

    balance = 1000

    while True:

        choice = main_menu()

        if choice == 1:
            show_balance(balance)

        elif choice == 2:
            amount = get_amount("Deposit Amount: ")
            balance = deposit(balance, amount)
            print("Deposit successful.")

        elif choice == 3:
            amount = get_amount("Withdraw Amount: ")

            if amount <= balance:
                balance = withdraw(balance, amount)
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")

        elif choice == 4:
            print("Goodbye!")
            break


main()