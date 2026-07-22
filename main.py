import json
from todolist import (
    add_task,
    complete_task,
    delete_task,
    list_tasks
)


def save_tasks(task_list, filename):
    """
    Saves tasks to a JSON file.
    """
    data = []

    for task in task_list:
        data.append({
            "title": task.title,
            "due_date": str(task.due_date) if task.due_date else None,
            "completed": task.completed
        })

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print("Tasks saved successfully.")


def display_menu():
    print("\n===== PERSONAL TO-DO LIST MANAGER =====")
    print("(A) Add a new task")
    print("(C) Mark a task as completed")
    print("(D) Delete a task")
    print("(L) List all tasks")
    print("(Q) Quit")


def main():
    task_list = []

    while True:
        display_menu()

        choice = input("\nEnter your choice: ").strip().upper()

        if choice == "A":
            title = input("Enter task title: ")

            due_date = input(
                "Enter due date (YYYY-MM-DD) or press Enter to skip: "
            ).strip()

            if due_date == "":
                due_date = None

            add_task(task_list, title, due_date)

        elif choice == "C":
            list_tasks(task_list)

            try:
                index = int(
                    input("Enter the task index to mark as completed: ")
                )
                complete_task(task_list, index)

            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "D":
            list_tasks(task_list)

            try:
                index = int(
                    input("Enter the task index to delete: ")
                )
                delete_task(task_list, index)

            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "L":
            list_tasks(task_list)

        elif choice == "Q":
            save_choice = input(
                "Would you like to save your tasks before quitting? (Y/N): "
            ).strip().upper()

            if save_choice == "Y":
                filename = input(
                    "Enter filename (e.g., tasks.json): "
                ).strip()

                save_tasks(task_list, filename)

            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose A, C, D, L, or Q.")


if __name__ == "__main__":
    main()