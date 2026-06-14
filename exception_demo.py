def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Test safe_divide with try/except/finally
try:
    result = safe_divide(10, 0)  # Change 0 to another number to test success
    print("Result:", result)

except ValueError as error:
    print("Error:", error)

finally:
    print("Division operation completed")


# Demonstrate catching a generic exception
try:
    number = int("abc")  # Invalid conversion

except Exception as error:
    print("A generic exception occurred:", error)