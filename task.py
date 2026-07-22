from datetime import date

from colorama import Fore, Style
from prettytable import PrettyTable


class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        status = "[X]" if self.completed else "[-]"

        if self.due_date:
            return f"{status} {self.title} (due {self.due_date})"
        else:
            return f"{status} {self.title}"
        
        from task import Task

task1 = Task("Submit assignment", "2026-07-31")
task2 = Task("Buy groceries")
task3 = Task("Pay bills", "2026-07-31", True)

print(task1)
print(task2)
print(task3)

def list_tasks(task_list):
    """
    Displays all tasks in a formatted table with color coding.
    """

    if not task_list:
        print("No tasks available.")
        return

    table = PrettyTable()
    table.field_names = [
        "Index",
        "Status",
        "Title",
        "Due Date",
        "Notes"
    ]

    today = date.today()

    for i, task in enumerate(task_list):

        status = "Completed" if task.completed else "Pending"

        due_date = (
            str(task.due_date)
            if task.due_date
            else "N/A"
        )

        note = ""

        if task.completed:
            row_color = Fore.GREEN

        elif task.due_date and task.due_date < today:
            row_color = Fore.RED
            note = "OVERDUE"

        else:
            row_color = Fore.YELLOW

        table.add_row([
            f"{row_color}{i}{Style.RESET_ALL}",
            f"{row_color}{status}{Style.RESET_ALL}",
            f"{row_color}{task.title}{Style.RESET_ALL}",
            f"{row_color}{due_date}{Style.RESET_ALL}",
            f"{row_color}{note}{    Style.RESET_ALL}"
        ])

    print("\nTASK LIST")
    print(table) 