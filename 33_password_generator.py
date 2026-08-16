"""
Project 33

Password Generator

A command-line password generator built with Python.

Features:

- Set password length
- Choose lowercase letters
- Choose uppercase letters
- Choose numbers
- Choose special characters
- Generate random passwords
- Generate multiple passwords

Concepts practiced:

- Functions
- Loops
- Conditional statements
- Dictionaries
- String processing
- Input validation
- Exception handling
- random module
- string module
- random.choice()
"""

import random
import string


def get_password_length():

    while True:
        try:
            length_input = input("Enter password length: ").strip()

            if not length_input:
                print("Password length cannot be empty.")
                continue

            length = int(length_input)

            if length < 8:
                print("Password length must be at least 8.")
                continue

            return length

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_character_options():

    while True:

        character_options = {
            "lowercase": False,
            "uppercase": False,
            "numbers": False,
            "special": False
        }

        while True:
            lower_input = input(
                "Include lowercase letters? (y/n): "
            ).strip().lower()

            if lower_input == "y":
                character_options["lowercase"] = True
                break

            elif lower_input == "n":
                break

            else:
                print("Please enter y or n.")

        while True:
            upper_input = input(
                "Include uppercase letters? (y/n): "
            ).strip().lower()

            if upper_input == "y":
                character_options["uppercase"] = True
                break

            elif upper_input == "n":
                break

            else:
                print("Please enter y or n.")

        while True:
            number_input = input(
                "Include numbers? (y/n): "
            ).strip().lower()

            if number_input == "y":
                character_options["numbers"] = True
                break

            elif number_input == "n":
                break

            else:
                print("Please enter y or n.")

        while True:
            special_input = input(
                "Include special characters? (y/n): "
            ).strip().lower()

            if special_input == "y":
                character_options["special"] = True
                break

            elif special_input == "n":
                break

            else:
                print("Please enter y or n.")

        if any(character_options.values()):
            return character_options

        print("You must select at least one character type.")


def generate_password(length, character_options):

    characters = ""

    if character_options["lowercase"]:
        characters += string.ascii_lowercase

    if character_options["uppercase"]:
        characters += string.ascii_uppercase

    if character_options["numbers"]:
        characters += string.digits

    if character_options["special"]:
        characters += string.punctuation

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():

    while True:

        length = get_password_length()

        character_options = get_character_options()

        password = generate_password(length, character_options)

        print(f"\nGenerated Password: {password}")

        while True:

            password_again = input(
                "Generate another password? (y/n): "
            ).strip().lower()

            if password_again == "y":
                break

            elif password_again == "n":
                print("Goodbye!")
                return

            else:
                print("Please enter y or n.")


if __name__ == "__main__":
    main()