def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        try:
            return divide(a, b)
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."
    else:
        return "Error: Invalid operation."


# Main program
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Choose an operation (+, -, *, /): ")

    result = calculate(num1, num2, operation)

    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numeric values.")