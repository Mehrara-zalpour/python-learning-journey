"""
Project 21

To-Do List (File Handling)

Description:
A simple command-line To-Do List application that allows
users to manage their daily tasks.

Features:
- Show all tasks
- Add new tasks
- Delete existing tasks
- File storage (tasks.txt)
- Input validation
- Functions
- Menu-driven program

Author: Mehrara
Date: 2026-07-25
"""

def main_menu():

    while True:
        try:
            choice = int(input("""

====== TO-DO LIST ======

1. Show Tasks
2. Add Task
3. Delete Task
4. Exit

Choose:  """))

            if 1 <= choice <= 4:
                return choice

            print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def show_tasks():
    print("\n===== Your Tasks =====")

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task.strip()}")


def add_task():
    new_task = input("Enter a new task: ")

    if not new_task:
        print("Task cannot be empty.")
        return

    with open("tasks.txt", "a") as file:
        file.write(new_task.strip() + "\n")

    print("Task added successfully.")


def delete_task():
    show_tasks()

    with open("tasks.txt", "r") as file:
        tasks = file.readlines()

    if not tasks:
        print("No tasks found.")
        return

    while True:
        try:
            del_choose = int(input("Enter task number: "))

            if 1 <= del_choose <= len(tasks):
                del tasks[del_choose - 1]
                break

            print("Please enter a valid task number.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task)

    print("Task deleted successfully.")


def main():

    while True:

        choice = main_menu()

        if choice == 1:
            show_tasks()

        elif choice == 2:
            add_task()

        elif choice == 3:
            delete_task()

        elif choice == 4:
            print("Goodbye!")
            break


main()
