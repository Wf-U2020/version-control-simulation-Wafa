# contact_book.py

def add_contact(contacts):
    name = input("Enter contact name: ").strip()

    if name in contacts:
        print("A contact with that name already exists.")
        return

    phone = input("Enter phone number: ").strip()

    if not phone.isdigit():
        print("Invalid phone number. Please enter digits only.")
        return

    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("The contact list is empty.")
        return

    print("\nContacts:")
    for name in sorted(contacts):
        print(f"Name: {name}, Phone: {contacts[name]}")


def search_contact(contacts):
    search_name = input("Enter a name to search: ").strip().lower()

    found = False

    for name, phone in contacts.items():
        if search_name in name.lower():
            print(f"Name: {name}, Phone: {phone}")
            found = True

    if not found:
        print("No matching contacts found.")


def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()

    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print("Contact not found.")


def display_menu():
    print("\nContact Book Menu")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    contacts = {}

    while True:
        display_menu()

        try:
            choice = int(input("Enter your choice (1-5): "))

            if choice == 1:
                add_contact(contacts)

            elif choice == 2:
                view_contacts(contacts)

            elif choice == 3:
                search_contact(contacts)

            elif choice == 4:
                delete_contact(contacts)

            elif choice == 5:
                print("Exiting Contact Book. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 5.")

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")

        except Exception as error:
            print("An unexpected error occurred:", error)


if __name__ == "__main__":
    main()