"""
Project 19

Number Guessing Game (Functions)

Description:
A simple number guessing game where the computer
chooses a random number and the player tries to guess it.

Features:
- Random number generation
- User guessing
- Higher / Lower hints
- Score (attempt counter)
- Input validation
- Functions
- Play again option

Author: Mehrara
Date: 2026-07-22
"""
import random


def choose_number():
    return (random.randint(1, 100))


def get_user_guess():
    while True:
        try:
            number = int(input("Enter Your Guess Number 1 / 100: "))
            if 1 <= number <= 100:
                return (number)

            print("Please Enter number 0 / 100 ")

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue


def play_game():

    machine = choose_number()
    attempts = 7

    while attempts > 0:

        user = get_user_guess()

        if user == machine:
            print("Correct!")
            return

        elif user < machine:
            print("Too Low!")

        else:
            print("Too High!")

        attempts -= 1
        print(f"Attempts Left: {attempts}")

    print(f"\nGame Over! The correct number was {machine}.")


def play_again():

    while True:

        answer = input("\nDo you want to continue? (y/n): ").lower()

        if answer == "y":
            play_game()
            return

        elif answer == "n":
            print("Goodbay!")
            

        else:
            print("Please enter only 'y' or 'n'.")


play_game()
play_again()

