import math
import random
import platform

# Generate a random integer between 1 and 100
random_number = random.randint(1, 100)

# Calculate the square root and round it down
square_root_floored = math.floor(math.sqrt(random_number))

# Retrieve system information
os_name = platform.system()
python_version = platform.python_version()

# Display results
print(f"Random Number: {random_number}")
print(f"Square Root (floored): {square_root_floored}")
print(f"Operating System: {os_name}")
print(f"Python Version: {python_version}")