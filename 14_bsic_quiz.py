"""
Project 14

Basic Quiz

Description:
A simple Python quiz game that asks the user
multiple questions and calculates the final score.

Features:
- Multiple-choice questions
- Score calculation
- Input validation
- Final result
- Play again option

Author: Mehrara
Date: 2026-07-18
"""

running = True


while running:

    score = 0

    while True:
        try:
            quiz1 = int(input("""
                    Question 1:
                    What is the capital of France?

                    1. Berlin
                    2. Madrid
                    3. Paris
                    4. Rome  

                    Your answer:          
                         """))

            if 1 <= quiz1 <= 4:
                if quiz1 == 3:
                    score += 1
                    print(f"Your answer: {quiz1}\nCorrect!")
                    break

                print("\nIt is Wrong!\ncorrect answer : 3")
                break

            print("choice number 1 - 4")
            continue

        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            quiz2 = int(input("""
                Question 2:
                What is the capital of Iran?

                1. Berlin
                2. Tehran
                3. Paris
                4. Rome  

                Your answer              
                    """))

            if 1 <= quiz2 <= 4:
                if quiz1 == 2:
                    score += 1
                    print(f"Your answer: {quiz2}\nCorrect!")
                    break

                print("\nIt is Wrong!\ncorrect answer : 2")
                break
            print("choice number 1 - 4")
            continue
    
        except ValueError:
            print("Invalid input. Please enter a number.")   
             
    print(f"\nYour Score: {score}/2")

    while True:
        answer = input("\nDo you want to play again? (y/n): ").lower()

        if answer == "y":
            break

        elif answer == "n":
            running = False
            print("Good bye!")
            break

        else:
            print("Please enter only 'y' or 'n'.")
