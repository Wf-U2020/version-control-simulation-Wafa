
numbers = []

while True:
    print("\nList Manager Menu")
    print("a) Add a number")
    print("b) Remove a number")
    print("c) Display the list")
    print("d) Quit")

    choice = input("Choose an option (a/b/c/d): ").lower()

    if choice == "a":
        try:
            number = int(input("Enter an integer to add: "))
            numbers.append(number)
            print(f"{number} added to the list.")
        except ValueError:
            print("Error: Please enter a valid integer.")

    elif choice == "b":
        try:
            index = int(input("Enter the index to remove: "))
            removed = numbers.pop(index)
            print(f"Removed {removed} from the list.")
        except ValueError:
            print("Error: Index must be an integer.")
        except IndexError:
            print("Error: Invalid index. No item exists at that position.")

    elif choice == "c":
        print("Current list:", numbers)

    elif choice == "d":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Error: Invalid menu option. Please choose a, b, c, or d.")