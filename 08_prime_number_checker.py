"""
Project 08

Prime Number Checker

Description:
A simple Python program that checks whether
a number is prime or not.

Features:
- Prime number detection
- Input validation
- User-defined number
- Play again option

Author: Mehrara
Date: 2026-07-14
"""

running = True

while running:

    while True:
        try:
            number = int(input("Enter a number: "))

            if number <= 1:
                print("This number is not prime.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"\n{number} is a prime number.")
    else:
        print(f"\n{number} is not a prime number.")

    while True:
        answer = input("Do you want to continue? (y/n): ").lower()

        if answer == "y":
            break

        elif answer == "n":
            running = False
            print("Goodbye!")
            break

        else:
            print("Please enter only 'y' or 'n'.")