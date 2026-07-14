"""
Project 07

Multiplication Table

Description:
A simple Python program that generates the multiplication
table of a number entered by the user.

Features:
- Generate multiplication table
- User-defined number
- Input validation
- Play again option

Author: Mehrara
Date: 2026-07-14
"""

running = True

while running:

    while True:
        try:
            number = int(input("Enter a number:  "))
            limit = int(input("Enter maximum multiplier: "))

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        print(f"\nMultiplication Table of {number}\n")

        for i in range(1, limit + 1):
            multi = number * i
            print(f"{number} * {i} = {multi}")

        while True:
            answer = input(
                "Do you want to generate another multiplication table? (y/n):  ").lower()

            if answer == "y":
                break

            elif answer == "n":
                running = False
                print("Goodbye!")
                break

            else:
                print("Please enter only 'y' or 'n'.")

        break
