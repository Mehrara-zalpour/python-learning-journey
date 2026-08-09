"""
Project 27

Inventory Manager

A command-line inventory management application built with Python.

Features:

- Add products
- View products
- Update products
- Delete products
- Search products by ID
- Sort products by name, price, quantity, or category
- Find low-stock products
- Store data in a CSV file

Concepts practiced:

- Functions
- Lists and dictionaries
- File handling
- CSV module
- Exception handling
- Input validation
- sorted() and lambda
"""

import csv


FILE_NAME = "products.csv"


def main_menu():
    while True:
        try:
            choice = int(input("""
====== INVENTORY MANAGER ======

1. View Products
2. Add Product
3. Update Product
4. Delete Product
5. Search Product
6. Sort Products
7. Low Stock Products
8. Exit

Choose an option: """))

            if 1 <= choice <= 8:
                return choice

            print("Please enter a number between 1 - 8.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def load_products():
    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    except FileNotFoundError:
        return []


def save_products(products):
    fieldnames = [
        "id",
        "name",
        "category",
        "price",
        "quantity"
    ]

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(products)


def get_next_id(products):
    if not products:
        return 1

    ids = [int(product["id"]) for product in products]

    return max(ids) + 1


def display_product(product):
    print("\n--------------------")
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Category: {product['category']}")
    print(f"Price: {product['price']}")
    print(f"Quantity: {product['quantity']}")
    print("--------------------")


def get_product_id():
    while True:
        product_id = input("Enter Product ID: ").strip()

        if not product_id:
            print("Product ID cannot be empty.")
            continue

        if not product_id.isdigit():
            print("Please enter a valid ID.")
            continue

        return product_id


def get_product_name():
    while True:
        name = input("Enter product name: ").strip()

        if name:
            return name

        print("Product name cannot be empty.")


def get_category():
    while True:
        category = input("Enter category: ").strip()

        if category:
            return category

        print("Category cannot be empty.")


def get_price():
    while True:
        try:
            price = float(input("Enter price: "))

            if price >= 0:
                return price

            print("Price cannot be negative.")

        except ValueError:
            print("Please enter a valid price.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity >= 0:
                return quantity

            print("Quantity cannot be negative.")

        except ValueError:
            print("Please enter a valid quantity.")


def view_products():
    print("\n===== Your Products =====")

    products = load_products()

    if not products:
        print("No products found.")
        return

    for product in products:
        display_product(product)


def add_product():
    print("\n===== Add Product =====")

    products = load_products()

    name = get_product_name()
    category = get_category()
    price = get_price()
    quantity = get_quantity()

    product_id = get_next_id(products)

    product = {
        "id": product_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }

    products.append(product)

    save_products(products)

    print("Product added successfully!")


def update_product():
    print("\n===== Update Product =====")

    products = load_products()

    if not products:
        print("No products found.")
        return

    view_products()

    product_id = get_product_id()

    for product in products:

        if product["id"] == product_id:

            new_name = get_product_name()
            new_category = get_category()
            new_price = get_price()
            new_quantity = get_quantity()

            product["name"] = new_name
            product["category"] = new_category
            product["price"] = new_price
            product["quantity"] = new_quantity

            save_products(products)

            print("Product updated successfully!")
            return

    print("Product not found.")


def delete_product():
    print("\n===== Delete Product =====")

    products = load_products()

    if not products:
        print("No products found.")
        return

    view_products()

    product_id = get_product_id()

    for product in products:

        if product["id"] == product_id:

            products.remove(product)

            save_products(products)

            print("Product deleted successfully.")
            return

    print("Product not found.")


def search_product():
    print("\n===== Search Product =====")

    products = load_products()

    if not products:
        print("No products found.")
        return

    product_id = get_product_id()

    for product in products:

        if product["id"] == product_id:
            display_product(product)
            return

    print("Product not found.")


def sort_products():
    while True:
        try:
            choice_number = int(input("""
===== Sort Products =====

1. Sort by Name
2. Sort by Price
3. Sort by Quantity
4. Sort by Category
5. Back

Choose: """))

            if 1 <= choice_number <= 5:
                break

            print("Please enter a number between 1 - 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice_number == 5:
        return

    products = load_products()

    if not products:
        print("No products found.")
        return

    if choice_number == 1:
        sorted_products = sorted(
            products,
            key=lambda product: product["name"].lower()
        )

    elif choice_number == 2:
        sorted_products = sorted(
            products,
            key=lambda product: float(product["price"])
        )

    elif choice_number == 3:
        sorted_products = sorted(
            products,
            key=lambda product: int(product["quantity"])
        )

    else:
        sorted_products = sorted(
            products,
            key=lambda product: product["category"].lower()
        )

    for product in sorted_products:
        display_product(product)


def low_stock_products():
    print("\n===== Low Stock Products =====")

    while True:
        try:
            stock_limit = int(
                input(
                    "Enter the maximum stock level for low-stock products: "
                )
            )

            if stock_limit >= 0:
                break

            print("Please enter a number 0 or greater.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    products = load_products()

    if not products:
        print("No products found.")
        return

    found = False

    for product in products:

        if int(product["quantity"]) <= stock_limit:
            found = True
            print(
                f"Product: {product['name']}, "
                f"Quantity: {product['quantity']}"
            )

    if not found:
        print("No low-stock products found.")


def main():
    while True:

        choice = main_menu()

        if choice == 1:
            view_products()

        elif choice == 2:
            add_product()

        elif choice == 3:
            update_product()

        elif choice == 4:
            delete_product()

        elif choice == 5:
            search_product()

        elif choice == 6:
            sort_products()

        elif choice == 7:
            low_stock_products()

        elif choice == 8:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

    28 — Weather CLI
