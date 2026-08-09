"""
TO-DO LIST PRO

Project 26 - Python Learning Journey

Features:
- Create tasks
- View tasks
- Update tasks
- Complete tasks
- Search tasks
- Delete tasks
- Show today's tasks

Concepts practiced:
- Dictionary
- Nested Dictionary
- JSON
- File Handling
- CRUD Operations
- Functions
- Exception Handling
- Input Validation
- datetime module
"""

import json
from datetime import datetime


FILE_NAME = "tasks.json"


def main_menu():
    """
    Display main menu and get user choice.
    """

    while True:
        try:
            choice = int(input("""
====== TO-DO LIST PRO ======

1. View Tasks
2. Add Task
3. Complete Task
4. Search Task
5. Delete Task
6. Show Today's Tasks
7. Update Task
8. Exit

Choose an option: """))

            if 1 <= choice <= 8:
                return choice

            print("Please enter a number between 1 - 8.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def load_tasks():
    """
    Load tasks from JSON file.
    If file does not exist or data is invalid,
    return an empty dictionary.
    """

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_tasks(tasks):
    """
    Save tasks into JSON file.
    """

    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def get_next_task_id(tasks):
    """
    Generate a unique task ID.

    It prevents duplicate IDs after deleting tasks.
    """

    if not tasks:
        return 1

    ids = [int(task_id) for task_id in tasks.keys()]

    return max(ids) + 1


def view_tasks():
    """
    Display all tasks.
    """

    print("\n===== Your Tasks =====")

    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    for task_id, task in tasks.items():

        print("\n--------------------")
        print(f"ID: {task['id']}")
        print(f"Title: {task['title']}")
        print(f"Description: {task['description']}")
        print(f"Created At: {task['created_at']}")
        print(f"Deadline: {task['deadline']}")
        print(f"Priority: {task['priority']}")
        print(f"Status: {task['status']}")
        print("--------------------")


def add_task():
    """
    Create a new task and save it.
    """

    print("\n===== Add Task =====")

    while True:
        title = input("Enter task title: ").strip()

        if title:
            break

        print("Title cannot be empty.")

    while True:
        description = input("Enter task description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    while True:
        try:
            deadline = input(
                "Enter deadline (YYYY-MM-DD): "
            ).strip()

            deadline = datetime.strptime(
                deadline,
                "%Y-%m-%d"
            )

            break

        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    while True:
        try:
            priority = int(input("""
1. High
2. Medium
3. Low

Choose priority (1/2/3): """))

            if priority == 1:
                priority = "High"
                break

            elif priority == 2:
                priority = "Medium"
                break

            elif priority == 3:
                priority = "Low"
                break

            else:
                print("Please choose between 1 and 3.")

        except ValueError:
            print("Please enter a number.")

    tasks = load_tasks()

    task_id = get_next_task_id(tasks)

    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "created_at": datetime.now().strftime("%Y-%m-%d"),
        "deadline": deadline.strftime("%Y-%m-%d"),
        "priority": priority,
        "status": "Pending"
    }

    tasks[str(task_id)] = task

    save_tasks(tasks)

    print("Task added successfully.")


def complete_task():
    """
    Change task status from Pending to Completed.
    """

    print("\n===== Complete Task =====")

    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    view_tasks()

    task_id = input("Enter task ID: ").strip()

    if task_id in tasks:

        tasks[task_id]["status"] = "Completed"

        save_tasks(tasks)

        print("Task completed successfully.")

    else:
        print("Task not found.")


def search_task():
    """
    Search tasks by title.
    """

    print("\n===== Search Task =====")

    title = input(
        "Enter title to search: "
    ).strip()

    if not title:
        print("Search title cannot be empty.")
        return

    tasks = load_tasks()

    found = False

    for task_id, task in tasks.items():

        if title.lower() in task["title"].lower():

            found = True

            print("\n--------------------")
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Deadline: {task['deadline']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print("--------------------")

    if not found:
        print("Task not found.")


def update_task():
    """
    Update an existing task.
    """

    print("\n===== Update Task =====")

    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    view_tasks()

    task_id = input("Enter task ID: ").strip()

    if task_id not in tasks:
        print("Task not found.")
        return

    while True:
        title = input("Enter new title: ").strip()

        if title:
            break

        print("Title cannot be empty.")

    description = input(
        "Enter new description: "
    ).strip()

    while True:
        try:
            deadline = input(
                "Enter new deadline (YYYY-MM-DD): "
            ).strip()

            deadline = datetime.strptime(
                deadline,
                "%Y-%m-%d"
            )

            break

        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    while True:
        try:
            priority = int(input("""
1. High
2. Medium
3. Low

Choose new priority (1/2/3): """))

            if priority == 1:
                priority = "High"
                break

            elif priority == 2:
                priority = "Medium"
                break

            elif priority == 3:
                priority = "Low"
                break

            else:
                print("Please choose between 1 and 3.")

        except ValueError:
            print("Please enter a number.")

    tasks[task_id]["title"] = title
    tasks[task_id]["description"] = description
    tasks[task_id]["deadline"] = deadline.strftime("%Y-%m-%d")
    tasks[task_id]["priority"] = priority

    save_tasks(tasks)

    print("Task updated successfully.")


def delete_task():
    """
    Delete a task by ID.
    """

    print("\n===== Delete Task =====")

    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    view_tasks()

    task_id = input(
        "Enter task ID: "
    ).strip()

    if task_id not in tasks:
        print("Task not found.")
        return

    confirm = input(
        "Are you sure you want to delete this task? (y/n): "
    ).lower()

    if confirm == "y":

        del tasks[task_id]

        save_tasks(tasks)

        print("Task deleted successfully.")

    else:
        print("Delete cancelled.")


def show_today_tasks():
    """
    Display tasks that have today's deadline.
    """

    print("\n===== Today's Tasks =====")

    tasks = load_tasks()

    if not tasks:
        print("No tasks found.")
        return

    today = datetime.now().strftime("%Y-%m-%d")

    found = False

    for task_id, task in tasks.items():

        if today == task["deadline"]:

            found = True

            print("\n--------------------")
            print(f"ID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Deadline: {task['deadline']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print("--------------------")

    if not found:
        print("No tasks scheduled for today.")


def main():
    """
    Run the application.
    """

    while True:

        choice = main_menu()

        if choice == 1:
            view_tasks()

        elif choice == 2:
            add_task()

        elif choice == 3:
            complete_task()

        elif choice == 4:
            search_task()

        elif choice == 5:
            delete_task()

        elif choice == 6:
            show_today_tasks()

        elif choice == 7:
            update_task()

        elif choice == 8:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
