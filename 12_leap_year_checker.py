"""
Project 12

Leap Year Checker

Description:
A simple Python program that checks whether
a given year is a leap year or not.

Features:
- Leap year detection
- User-defined year
- Input validation
- Play again option

Author: Mehrara
Date: 2026-07-16
"""

running = True


while running:

    while True:
        try:
            year = int(input("Enter a year:   "))

            if year < 1:
                print("Please enter a valid year.")
                continue
            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a Leap year") 
    else:
        print(f"{year} is not a Leap year")

        
    while True:
        answer = input("\nDo you want to continue? (y/n): ").lower()

        if answer == "y":
            break

        elif answer == "n":
            running = False
            print("Good bye!")
            break

        else:
            print("Please enter only 'y' or 'n'.")
