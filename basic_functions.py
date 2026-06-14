
def greet_user(name=""):
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Hello! Welcome!")

# Examples
greet_user("Alice")
 # Output: Hello, Alice! Welcome!
greet_user()
greet_user("")

def add_two_numbers(a, b):
    return a + b


def is_even(num):
    return num % 2 == 0


# Examples
print(add_two_numbers(5, 3))  # Output: 8

print(is_even(4))  # Output: True
print(is_even(7))  # Output: False