def get_average_grade(grades_tuple):
    try:
        average = sum(grades_tuple) / len(grades_tuple)
        return average
    except ZeroDivisionError:
        print("Warning: Cannot calculate average for an empty tuple of grades.")
        return None


# Dictionary of courses and their grades
course_grades = {
    "Math": (90, 85, 88, 92),
    "Science": (78, 82, 80, 85),
    "History": (95, 89, 91),
    "Art": ()  # Edge case: empty tuple
}

# Calculate and display average grades
for course, grades in course_grades.items():
    average = get_average_grade(grades)

    if average is not None:
        print(f"The average grade for {course} is {average:.1f}")
    else:
        print(f"No grades available for {course}.")