"""
Project 04

BMI Calculator

Description:
A simple Python program that calculates the Body Mass Index (BMI)
based on the user's height and weight, then displays the BMI category.

Features:
- Accepts height in meters or centimeters
- Accepts weight in kilograms
- Calculates BMI
- Displays the BMI category
- Handles invalid input
- Allows multiple calculations

Author: Mehrara
Date: 2026-07-13
"""


running = True

while running:

    try:
        height = float(input("Enter your height (m):  "))
        if height > 10:
            height_m = height / 100
        else:
            height_m = height

        weight = float(input("Enter your weight (kg):   "))

        if height > 0 and weight > 0:
            bmi = weight / (height_m ** 2)
            print(f"Your BMI is: {bmi:.2f}")

            if bmi < 18.5:
                print("Underweight")

            elif 18.5 <= bmi < 25:
                print("Normal weight")

            elif 25 < bmi < 30:
                print("Overweight")

            else:
                print("Obese")

            while True:
                answer = input("Do you want to continue? (y/n): ").lower()

                if answer == "y":
                    break

                elif answer == "n":
                    running = False
                    print("Goodbye!")
                    break

                else:
                    print("Please enter only 'y' or 'n'.")
        else:
            print("Height and weight must be greater than zero.")

    except ValueError:
        print("Invalid input. Please enter number")
