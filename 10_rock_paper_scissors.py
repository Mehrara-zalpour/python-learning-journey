"""
Project 10

Rock Paper Scissors

Description:
A simple Python game where the user plays
Rock, Paper, Scissors against the computer.

Features:
- Computer random choice
- User input validation
- Win / Lose / Draw detection
- Score counter
- Play again option

Author: Mehrara
Date: 2026-07-15
"""

import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

running = True

while running:

    print("\nChoose:")

    for i in range(len(choices)):
        print(f"{i + 1}. {choices[i]}")

    while True:
        try:
            user = int(input("\nEnter your choice (1-3): "))

            if 1 <= user <= 3:
                break

            print("Please enter a number between 1 and 3.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    player = choices[user - 1]
    computer = random.choice(choices)

    print(f"\nYou: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("\nIt's a draw!")

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        player_score += 1
        print("\nYou win!")

    else:
        computer_score += 1
        print("\nComputer wins!")

    print(f"\nScore")
    print(f"Player   : {player_score}")
    print(f"Computer : {computer_score}")

    while True:
        answer = input("\nDo you want to play again? (y/n): ").lower()

        if answer == "y":
            break

        elif answer == "n":
            running = False

            print("\nFinal Score")
            print(f"Player   : {player_score}")
            print(f"Computer : {computer_score}")
            print("\nThanks for playing!")

            break

        else:
            print("Please enter only 'y' or 'n'.")