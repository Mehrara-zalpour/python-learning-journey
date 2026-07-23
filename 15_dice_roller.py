"""
Project 15

Dice Roller

Description:
A simple Python program that simulates rolling
one or more dice.

Features:
- Random dice rolling
- User-defined number of rolls
- Input validation
- Play again option

Author: Mehrara
Date: 2026-07-18
"""
import random

running = True

while running:

    rolls = []

    while True:
        try:
            time_roll = int(input("How many times?   "))

            if time_roll > 0:
                break
            
            print("Please enter a number greater than 1.")
            

        except ValueError:
            print("Invalid input. Please enter a number.")

    for i in range(time_roll):
        roll_mashin = random.randint(1, 6)
        rolls.append(roll_mashin)
        print(f"Roll {i+1} = {roll_mashin}")
    
    print(f"Total = {sum(rolls)}")
    print(f"Avrage = {sum(rolls) / time_roll}")
    print(f"Highest Roll = {max(rolls)}")
    print(f"Lowest Roll = {min(rolls)}")

        
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
