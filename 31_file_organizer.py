"""
Project 31

File Organizer

A command-line file organization application built with Python.

Features:

- Select a folder
- List files and folders
- Identify file types by their extensions
- Create category folders automatically
- Organize files into categories
- Move files to their appropriate folders

Concepts practiced:

- Functions
- File and folder handling
- The os module
- The shutil module
- File paths
- os.path.join()
- os.path.isfile()
- os.path.isdir()
- os.path.splitext()
- os.makedirs()
- shutil.move()
- Lists
- Loops
- Input validation
"""

import os
import shutil


def get_folder():
    while True:
        folder_path = input("Enter a folder: ").strip()

        if not folder_path:
            print("Folder cannot be empty.")
            continue

        if not os.path.isdir(folder_path):
            print("Folder not found.")
            continue

        return folder_path


def get_files(folder_path):
    files = []

    items = os.listdir(folder_path)

    if not items:
        print("Folder is empty.")
        return files

    for item in items:
        file_path = os.path.join(folder_path, item)

        if not os.path.isfile(file_path):
            continue

        files.append(item)

    return files


def get_category(file_name):
    name, extension = os.path.splitext(file_name)

    if extension in [".jpg", ".jpeg", ".png", ".gif"]:
        return "Images"

    elif extension in [".pdf", ".doc", ".docx", ".txt"]:
        return "Documents"

    elif extension in [".mp3", ".wav"]:
        return "Music"

    elif extension in [".mp4", ".avi", ".mkv"]:
        return "Videos"

    elif extension == ".py":
        return "Python"

    elif extension == ".csv":
        return "CSV"

    else:
        return "Others"


def create_folders(folder_path):
    categories = [
        "Images",
        "Documents",
        "Music",
        "Videos",
        "Python",
        "CSV",
        "Others"
    ]

    for category in categories:
        category_path = os.path.join(folder_path, category)

        os.makedirs(category_path, exist_ok=True)


def organize_files(folder_path):
    files = get_files(folder_path)

    for file_name in files:
        category = get_category(file_name)

        source_path = os.path.join(folder_path, file_name)
        category_path = os.path.join(folder_path, category)
        destination_path = os.path.join(category_path, file_name)

        shutil.move(source_path, destination_path)

        print(f"Moved: {file_name} → {category}")


def main():
    folder_path = get_folder()
    create_folders(folder_path)
    organize_files(folder_path)


if __name__ == "__main__":
    main()
