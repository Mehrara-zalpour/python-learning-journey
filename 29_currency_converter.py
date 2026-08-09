"""
Project 29

Currency Converter

A command-line currency converter built with Python.

Features:

* Get an amount from the user
* Get source and target currencies
* Convert currencies using a real-time exchange rate API
* Display the converted amount and exchange rate
* Validate user input
* Handle API and data errors
* Prevent the program from crashing when an error occurs

Concepts practiced:

* Functions
* User input
* Input validation
* while loops
* continue and return
* try/except
* ValueError
* HTTP requests
* REST APIs
* JSON data
* Dictionaries
* API response handling
* HTTP status codes
* requests.raise_for_status()
* RequestException
* f-strings
* float conversion
* String methods
* Formatting numbers with decimal places

Libraries:

* requests

API:

* Frankfurter API

Project goal:

Practice working with external APIs, converting real-world data
into useful results, and handling errors safely in a Python CLI
application.
"""

import requests


def get_amount():
    while True:
        amount_input = input("Enter amount: ").strip()

        if not amount_input:
            print("Amount cannot be empty.")
            continue

        try:
            amount = float(amount_input)

            if amount <= 0:
                print("Enter a number greater than 0.")
                continue

            return amount

        except ValueError:
            print("Invalid input. Please enter a number.")


def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.frankfurter.dev/v2/rate/{from_currency}/{to_currency}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        rate = data["rate"]
        converted_amount = amount * rate

        print("\n===== CONVERSION RESULT =====")
        print(
            f"{amount:.2f} {from_currency} = "
            f"{converted_amount:.2f} {to_currency}"
        )
        print(f"Exchange rate: {rate}")

    except requests.exceptions.RequestException as error:
        print(f"API Error: {error}")

    except (KeyError, ValueError):
        print("Invalid data received from the API.")


def main():
    print("===== CURRENCY CONVERTER =====")

    amount = get_amount()

    from_currency = input("From currency: ").strip().upper()
    to_currency = input("To currency: ").strip().upper()

    convert_currency(amount, from_currency, to_currency)


if __name__ == "__main__":
    main()
