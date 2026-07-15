"""
Project 09

Unit Converter

Description:
A simple Python program that converts units
between different measurement systems.

Features:
- Multiple conversion options
- User-defined values
- Input validation
- Menu system
- Play again option

Author: Mehrara
Date: 2026-07-15
"""

menu = """
    Choose Conversion

1. Kilometers ➜ Miles
2. Miles ➜ Kilometers
3. Kilograms ➜ Pounds
4. Pounds ➜ Kilograms
5. Centimeters ➜ Inches
6. Inches ➜ Centimeters
    """

running = True

while running:

    print(menu)

    while True:
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                km = float(input("Enter distance:  "))
                miles = km * 0.621371
                print(f"{km} Kilometers is {miles:.2f} miles.")
                break

            elif choice == 2:
                mile = float(input("Enter distance:  "))
                km = mile * 1.60934
                print(f"{mile} miles is {km:.2f} Kilometers.")
                break

            elif choice == 3:
                kg = float(input("Enter weight:  "))
                po = kg * 2.20462
                print(f"{kg}kilograms is {po:.2f} pounds.")
                break

            elif choice == 4:
                pound = float(input("Enter weight:  "))
                kilo = pound * 0.453592
                print(f"{pound}pounds is {kilo:.2f} kilograms.")
                break

            elif choice == 5:
                cm = float(input("Enter Size:  "))
                inch = cm * 0.393701
                print(f"{cm} Centimeters is {inch:.2f} Inches.")
                break

            elif choice == 6:
                inc = float(input("Enter Size:  "))
                cant = inc * 2.54
                print(f"{inc} Inches is {cant:.2f} Centimeters.")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                break

        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 6.")
            continue

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
