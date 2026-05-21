#Ask the user for two numbers
num1_input = input("Enter the first number: ")
num2_input = input("Enter the second number: ")

#check if the inputs are valid numbers
try:
    num1 = float(num1_input)
    num2 = float(num2_input)

    #Ask the user for the operation they want to perform
    operation = input("Enter the operation (+, -, *, /): ")

    #Perform the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            exit()      
        result = num1 / num2
    else:
        print("Invalid operation.")
        exit()

    #Display the result
    if result is not None:
        print(f"The result of {num1} {operation} {num2} is: {result}")
    print(f"The result is: {result}")
except ValueError:
    print("Please enter valid numbers.")