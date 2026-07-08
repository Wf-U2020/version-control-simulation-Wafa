# Prompt the user to enter a sentence
sentence = input("Enter a sentence: ")

# Convert the sentence to uppercase and print it
print("Uppercase:", sentence.upper())

# Print the sentence in reverse order
print("Reversed:", sentence[::-1])

# Count the number of vowels (a, e, i, o, u)
vowel_count = 0
for char in sentence.lower():
    if char in "aeiou":
        vowel_count += 1

print("Number of vowels:", vowel_count)

# Replace spaces with hyphens
modified_sentence = sentence.replace(" ", "-")
print("Modified string:", modified_sentence)