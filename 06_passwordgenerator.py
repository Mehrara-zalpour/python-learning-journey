"""
Project 06

Password Generator

Description:
A simple Python program that generates a random password
based on the length entered by the user.

Features:
- Random password generation
- User-defined password length
- Input validation
- Play again option

Author: Mehrara
Date: 2026-07-14
"""

import string
import random

running = True

while running:
    
    password = ""

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length must be at least 4.")
            else:
                break
            
        except ValueError:
                print("Invalid input. Please enter a valid number.")



    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    for i in range(length):
        password += random.choice(characters)

    print(f"\nGenerated Password: {password}")

    while True:
        answer = input("Do you want to generate another password? (y/n): ").lower()

        if answer == "y":
            break
                
        elif answer =="n":
            running = False
            print("Goodbye!")
            break
                
        else:
            print("Please enter only 'y' or 'n'.")
                    
                    
                      



