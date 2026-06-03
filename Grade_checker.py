
# Asks the user to input a numeric grade (0-100)
grade = int(input("Enter a numeric grade (0-100): "))
#Uses an if-elif-else structure to convert the numeric grade to a letter grade
if grade >= 90:

    letter_grade = "A"
elif grade >= 80:
    letter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >= 60:
    letter_grade = "D"
elif grade >= 0:
    letter_grade = "F"
else:
    letter_grade = "Invalid"

#print(f"The letter grade is: {letter_grade}")

print ("Your grade is: " + letter_grade)
# Conditional expression for final message
message = (
    "Congratulations! You passed with a great grade!"
    if letter_grade in ["A", "B", "C"]
    else "Keep working hard and try again next time."
)

if letter_grade != "Invalid":
    print(message)
else:
    print("Please enter a grade between 0 and 100.")
