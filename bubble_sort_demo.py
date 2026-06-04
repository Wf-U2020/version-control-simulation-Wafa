# Bubble Sort Example

numbers = [64, 25, 12, 22, 11]

print("Original list:", numbers)

n = len(numbers)

# Bubble Sort
for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            # Swap elements
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # Print the list after each pass
    print(f"After pass {i + 1}: {numbers}")

# Print the final sorted list
print("Sorted list:", numbers)