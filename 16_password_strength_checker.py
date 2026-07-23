"""
Project 16

Password Strength Checker

Description:
A simple Python program that checks the strength
of a password based on several security rules.

Features:
- Password strength analysis
- Length validation
- Uppercase detection
- Lowercase detection
- Digit detection
- Special character detection
- Play again option

Author: Mehrara
Date: 2026-07-18
"""

running = True

while running:

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    password = input("Enter your password: ")

    if len(password) < 8:
        print("\nPassword is too short. (Minimum 8 characters)\n")

    else:

        for char in password:

            if char.isupper():
                has_upper = True

            elif char.islower():
                has_lower = True

            elif char.isdigit():
                has_digit = True

            else:
                has_special = True

        score = 0

        if has_upper:
            score += 1

        if has_lower:
            score += 1

        if has_digit:
            score += 1

        if has_special:
            score += 1

        print("\nPassword Analysis")

        print(f"Uppercase : {'✓' if has_upper else '✗'}")
        print(f"Lowercase : {'✓' if has_lower else '✗'}")
        print(f"Digit     : {'✓' if has_digit else '✗'}")
        print(f"Special   : {'✓' if has_special else '✗'}")

        if score == 4:
            print("\nPassword Strength: Strong 💪")

        elif score >= 2:
            print("\nPassword Strength: Medium 🙂")

        else:
            print("\nPassword Strength: Weak ⚠️")

    while True:

        answer = input("\nDo you want to continue? (y/n): ").lower()

        if answer == "y":
            break

        elif answer == "n":
            running = False
            print("Goodbye!")
            break

        else:
            print("Please enter only 'y' or 'n'.")