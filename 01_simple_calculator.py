menu = """
+
-
*
/
"""

# گرفتن عدد اول
while True:
    try:
        num1 = int(input("Enter Your Number1: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

# گرفتن عدد دوم
while True:
    try:
        num2 = int(input("Enter Your Number2: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

print(menu)

# گرفتن عملگر
while True:
    operator = input("Enter Your Choice: ")

    if operator in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid operator.")

# انجام محاسبه
if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 == 0:
        print("You cannot divide by zero.")
    else:
        print("Result =", num1 / num2)