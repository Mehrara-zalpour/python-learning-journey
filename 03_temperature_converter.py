"""
Project 03

Temperature Converter

Description:
A simple Python program that converts temperatures
between Celsius and Fahrenheit.

Author: Mehrara
Date: 2026-07-13
"""

menu = """
    Choose Conversion

    1. Celsius to Fahrenheit

    2. Fahrenheit to Celsius
    """

running = True

while running:
    print(menu)
    try:
        choice = input("Enter your choice: ")

        if choice == "1":
            temp_f = float(input("Enter Celsius Temperature: "))
            f = (temp_f * 9 / 5) + 32
            print(f"{f:.2f} Fahrenheit.")

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

        elif choice == "2":
            temp_c = float(input("Enter Fahrenheit Temperature: "))
            c = (temp_c - 32) * 5 / 9
            print(f"{c:.2f} Calsius.")

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
        
        else:
            print("Invalid choice. Please enter 1 or 2.\n")

    
    except ValueError:
        print("Invalid input. Please enter 1 or 2.\n")



    