"""
Project 40 - Image Downloader

A command-line image downloader built with Python.

Features:
- Create an images folder
- Download images from URLs
- Save downloaded images locally
- View downloaded images
- Delete downloaded images

Concepts practiced:
- Functions
- requests
- pathlib
- HTTP requests
- HTTP status codes
- Binary files
- File handling
- Path management
- Input validation
- Exception handling
- enumerate()
"""

import requests
from pathlib import Path


def setup_folder():
    """Create the images folder if it does not exist."""

    image_folder = Path("images")
    image_folder.mkdir(exist_ok=True)

    return image_folder


def download_image(image_folder):
    """Download an image from a URL and save it in the images folder."""

    print("\n===== DOWNLOAD IMAGE =====")

    while True:
        url = input("Enter image URL: ").strip()

        if not url:
            print("Image URL cannot be empty.")
            continue

        break

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("Failed to download image.")
            return

    except requests.RequestException:
        print("Could not connect to the URL.")
        return

    while True:
        filename = input("Enter image name: ").strip()

        if not filename:
            print("Image name cannot be empty.")
            continue

        break

    file_path = image_folder / filename

    try:
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"Image downloaded successfully: {file_path}")

    except OSError:
        print("Could not save the image.")


def view_images(image_folder):
    """Display all downloaded images."""

    print("\n===== DOWNLOADED IMAGES =====")

    images = []

    for item in image_folder.iterdir():
        if item.is_file():
            images.append(item)

    if not images:
        print("No images found.")
        return

    for number, image in enumerate(images, start=1):
        print(f"{number}. {image.name}")


def delete_image(image_folder):
    """Delete a downloaded image."""

    print("\n===== DELETE IMAGE =====")

    images = []

    for item in image_folder.iterdir():
        if item.is_file():
            images.append(item)

    if not images:
        print("No images found.")
        return

    for number, image in enumerate(images, start=1):
        print(f"{number}. {image.name}")

    while True:
        try:
            choice = int(input("Choose an image: "))

            if choice < 1 or choice > len(images):
                print(
                    f"Please enter a number between 1 and {len(images)}."
                )
                continue

            break

        except ValueError:
            print("Invalid input. Please enter a number.")

    image = images[choice - 1]

    while True:
        confirmation = input(
            f"Are you sure you want to delete '{image.name}'? (y/n): "
        ).strip().lower()

        if confirmation == "y":
            break

        if confirmation == "n":
            print("Deletion cancelled.")
            return

        print("Please enter 'y' or 'n'.")

    try:
        image.unlink()
        print("Image deleted successfully.")

    except OSError:
        print("Could not delete the image.")


def main_menu(image_folder):
    """Display the main menu and handle user choices."""

    while True:
        print("""
===== IMAGE DOWNLOADER =====

1. Download Image
2. View Images
3. Delete Image
4. Exit
""")

        try:
            choice = int(input("Choose an option: "))

            if choice == 1:
                download_image(image_folder)

            elif choice == 2:
                view_images(image_folder)

            elif choice == 3:
                delete_image(image_folder)

            elif choice == 4:
                print("Goodbye! 👋")
                break

            else:
                print("Please enter a number between 1 and 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    """Run the Image Downloader application."""

    image_folder = setup_folder()
    main_menu(image_folder)


if __name__ == "__main__":
    main()