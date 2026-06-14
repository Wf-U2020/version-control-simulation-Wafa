# Create a tuple containing the names of the twelve months
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# Print the first and last month
print("First month:", months[0])
print("Last month:", months[-1])

# Demonstrate tuple immutability
try:
    months[0] = "NewMonth"
except TypeError as error:
    print("Tuples are immutable, error:", error)

# Create a dictionary of students and grades
students = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92,
    "Diana": 88
}

# Add a new student
students["Ethan"] = 95

print("\nAll students and grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

# Update an existing student's grade
students["Bob"] = 91

print("\nUpdated entry:")
print(f"Bob: {students['Bob']}")

# Print all students and grades in a formatted way
print("\nFormatted student list:")
for name, grade in students.items():
    print(f"{name}: {grade}")