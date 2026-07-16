"""
Project 11

Number Statistics

Description:
A simple Python program that collects numbers
from the user and displays basic statistics.

Features:
- User-defined numbers
- Calculate sum
- Calculate average
- Find minimum value
- Find maximum value
- Input validation
- Play again option

Author: Mehrara
Date: 2026-07-16
"""


running = True


while running:

    numbers = []

    while True:
        try:
            enter_num = int(input("How Many Numbers you want to enter?  "))

            if enter_num < 1:
                print("Please enter a positive number.")
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    

    try:
        for i in range(enter_num):
            number = int(input(f"Number {i + 1}: "))
            numbers.append(number)

        sum_num =sum(numbers)
        count_num = len(numbers)
        average_num = sum_num / count_num
        print(numbers)
        print(f"Count = {count_num}")
        print(f"Sum = {sum_num}")
        print(f"Max = {max(numbers)}")
        print(f"Min = {min(numbers)}")
        print(f"Average = {average_num}")
        break

    except ValueError:
        print("Invalid input. Please enter a number.")

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
