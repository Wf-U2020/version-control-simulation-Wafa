import os
from datetime import datetime

filename = "diary.txt"

try:
    # Check if diary.txt exists; create it if it doesn't
    if not os.path.exists(filename):
        with open(filename, "w") as file:
            file.write("=== My Diary ===\n\n")

    # Get diary entry from user
    entry = input("Enter your diary entry: ")

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Append entry to the file
    with open(filename, "a") as file:
        file.write(f"[{timestamp}]\n")
        file.write(f"{entry}\n\n")

    print("\nEntry saved successfully!")

    # Read and display the entire diary
    print("\n--- Diary Contents ---")
    with open(filename, "r") as file:
        contents = file.read()
        print(contents)

except FileNotFoundError:
    print("Error: The diary file could not be found.")
except PermissionError:
    print("Error: Permission denied while accessing the diary file.")
except OSError as e:
    print(f"File operation error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")