"""
Project 18

Stopwatch (CLI)

Description:
A simple command-line stopwatch that measures
the elapsed time between pressing Enter to start
and Enter to stop.

Features:
- Start timer
- Stop timer
- Elapsed time calculation
- Time formatting
- Play again option

Author: Mehrara
Date: 2026-07-19
"""

import time


running = True

while running:

    input("Press Enter to Start...")
    start = time.time()
    print("\nStopwatch Started!")

    input("Press Enter to Stop...")
    end = time.time()

    elapsed = end - start

    print(f"\nElapsed Time: {elapsed:.2f} seconds")        

    while True:

        answer = input("\nDo you want to continue? (y/n): ").lower()

        if answer == "y":
            break

        elif answer == "n":
            running = False
            print("Goodbye!")
            break

        else:
            print("Please enter only 'y' or 'n'.")