"""
Project 02

Even or Odd Checker

This program checks whether a number is even or odd.
It also validates user input and allows the user to
check multiple numbers.
"""

running = True

while running:
    try:
        number = int(input("Enter your number: "))

        if number % 2 == 0:
            print("The number is even.")
        else:
            print("The number is odd.")

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

    except ValueError:
        print("Invalid input. Please enter a valid integer.\n")