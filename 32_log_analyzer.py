"""
Project 32

Log Analyzer

A command-line log analysis application built with Python.

Features:

- Read log files
- Search and filter log entries
- Count log levels such as INFO, WARNING, and ERROR
- Extract specific information using regular expressions
- Display analysis results

Concepts practiced:

- Functions
- File handling
- Regular expressions
- The re module
- String processing
- Loops
- Lists and dictionaries
- Exception handling
- Input validation
"""

import os
import re


def main_menu():

    while True:

        choose_input = input("""
====== LOG ANALYZER ======

1. Show Log Statistics
2. Show Errors
3. Search Logs
4. Show IP Addresses
5. Exit

Choose an option: """).strip()

        if not choose_input:
            print("Choice cannot be empty.")
            continue

        try:
            choose = int(choose_input)

            if 1 <= choose <= 5:
                return choose

            print("Please enter a number between 1 and 5.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_log_file():

    while True:

        file_path = input("Enter log file path: ").strip()

        if not file_path:
            print("File path cannot be empty.")
            continue

        if not os.path.isfile(file_path):
            print("File not found or path is not a file.")
            continue

        return file_path


def read_log_file(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    return content


def count_log_levels(content):

    levels = re.findall(r"(INFO|ERROR|WARNING)", content)

    counts = {
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0
    }

    for level in levels:
        counts[level] += 1

    return counts


def show_errors(content):

    lines = content.splitlines()
    errors = []

    for line in lines:

        if re.search(r"ERROR", line):
            errors.append(line)

    return errors


def search_logs(content, keyword):

    results = []
    lines = content.splitlines()

    for line in lines:

        if keyword in line:
            results.append(line)

    return results


def extract_ips(content):

    pattern = r"\d+\.\d+\.\d+\.\d+"

    return re.findall(pattern, content)


def main():

    file_path = get_log_file()
    content = read_log_file(file_path)

    while True:

        choose = main_menu()

        if choose == 1:

            counts = count_log_levels(content)

            print("\n====== LOG STATISTICS ======")
            print(f"INFO: {counts['INFO']}")
            print(f"ERROR: {counts['ERROR']}")
            print(f"WARNING: {counts['WARNING']}")

        elif choose == 2:

            errors = show_errors(content)

            print("\n====== ERRORS ======")

            if not errors:
                print("No errors found.")

            else:
                for error in errors:
                    print(error)

        elif choose == 3:

            keyword = input("Enter keyword: ").strip()

            if not keyword:
                print("Keyword cannot be empty.")
                continue

            results = search_logs(content, keyword)

            print("\n====== SEARCH RESULTS ======")

            if not results:
                print("No matching logs found.")

            else:
                for result in results:
                    print(result)

        elif choose == 4:

            ips = extract_ips(content)

            print("\n====== IP ADDRESSES ======")

            if not ips:
                print("No IP addresses found.")

            else:
                for ip in ips:
                    print(ip)

        elif choose == 5:

            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
