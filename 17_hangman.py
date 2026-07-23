"""
Project 17

Hangman (CLI)

Description:
A simple command-line Hangman game where
the player guesses a hidden word one letter at a time.

Features:
- Random word selection
- Letter-by-letter guessing
- Correct and wrong letter tracking
- Remaining attempts counter
- Win / Lose detection
- Input validation
- Play again option

Author: Mehrara
Date: 2026-07-18
"""

import random

words = [
    "python",
    "banana",
    "computer",
    "orange",
    "keyboard",
    "milk",
    "lion"
]

running = True

while running:

    word = random.choice(words)

    guessed_letters = []
    wrong_letters = []

    attempts = 15

    while attempts > 0:

        print("\nWord: ", end="")

        for char in word:
            if char in guessed_letters:
                print(char, end=" ")
            else:
                print("_", end=" ")

        print(f"\nAttempts Left: {attempts}")
        print("Wrong Letters:", " ".join(wrong_letters))

        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters or guess in wrong_letters:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed_letters.append(guess)
            print("Correct!")

        else:
            wrong_letters.append(guess)
            attempts -= 1
            print("Wrong!")

        win = True

        for char in word:
            if char not in guessed_letters:
                win = False
                break

        if win:
            print(f"\nCongratulations! The word was '{word}'.")
            break

    else:
        print(f"\nGame Over! The word was '{word}'.")

    while True:

        answer = input("\nDo you want to play again? (y/n): ").lower()

        if answer == "y":
            break

        elif answer == "n":
            running = False
            print("Goodbye!")
            break

        else:
            print("Please enter only 'y' or 'n'.")