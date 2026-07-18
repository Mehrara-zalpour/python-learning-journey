"""
Project 13

Countdown Timer (CLI)

Description:
A simple command-line countdown timer that counts
down from a user-defined number of seconds.

Features:
- User-defined countdown time
- Countdown display
- Input validation
- Play again option

Author: Mehrara
Date: 2026-07-16
"""
import time

running = True


while running:

    while True:
        try:
            seconds = int(input("Enter seconds:   "))

            if seconds < 1:
                print("Please enter a positive number.")
                continue
            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nStarting countdown...\n")
    for i in range(seconds, 0, -1):
        print(f"{i} . . . ")
        time.sleep(1)
    print("\nTime's up! ⏰")
    
        
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
