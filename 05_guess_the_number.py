"""
Project 05

Guess the Number

Description:
A simple number guessing game where the computer generates
a random number and the player tries to guess it.

Features:
- Random number generation
- Input validation
- Hint system (Too high / Too low)
- Attempt counter
- Play again option

Author: Mehrara
Date: 2026-07-13
"""

import random

running = True

while running:

    number = random.randint(1, 100)
    count = 0

    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))

            if not 1 <= guess <= 100:
                print("Please enter a number between 1 and 100.")
                continue

            count += 1

            if guess == number:
                print(f"\nCongratulations!")
                print(f"You guessed the number in {count} attempt(s).\n")

                while True:
                    answer = input("Do you want to play again? (y/n): ").lower()

                    if answer == "y":
                        break

                    elif answer == "n":
                        running = False
                        print("Goodbye!")
                        break

                    else:
                        print("Please enter only 'y' or 'n'.")

                break

            elif guess > number:
                print(f"Too high! Attempts: {count}")

            else:
                print(f"Too low! Attempts: {count}")

        except ValueError:
            print("Invalid input. Please enter a valid number.")