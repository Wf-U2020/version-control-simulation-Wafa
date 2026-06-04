# Create a list of integers
numbers = [12, 5, 27, 8, 19]

# Print the original list
print("Original list:", numbers)

# Use sorted() to create a sorted copy without modifying the original list
sorted_numbers = sorted(numbers)
print("Sorted copy using sorted():", sorted_numbers)

# Show that the original list is unchanged
print("Original list after sorted():", numbers)

# Sort the list in place using .sort()
numbers.sort()
print("List after .sort():", numbers)

# Add a new element
numbers.append(15)
print("List after appending 15:", numbers)

# Remove an element by value
numbers.remove(8)
print("List after removing 8:", numbers)

# Reverse the list
numbers.reverse()
print("Reversed list:", numbers)