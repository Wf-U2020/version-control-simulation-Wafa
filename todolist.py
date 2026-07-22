from datetime import datetime, date
from task import Task


def add_task(task_list, title, due_date=None):
    """
    Creates a new Task and adds it to the task list.
    """

    parsed_date = None

    if due_date:
        try:
            parsed_date = datetime.strptime(
                due_date, "%Y-%m-%d"
            ).date()
        except ValueError:
            print("Error: Due date must be in YYYY-MM-DD format.")
            return

    task = Task(title, parsed_date)
    task_list.append(task)

    print("Task added successfully.")


def complete_task(task_list, index):
    """
    Marks the task at the specified index as completed.
    """

    try:
        task_list[index].completed = True
        print("Task marked as completed.")
    except IndexError:
        print("Error: Invalid task index.")


def delete_task(task_list, index):
    """
    Deletes the task at the specified index.
    """

    try:
        removed_task = task_list.pop(index)
        print(f"Deleted task: {removed_task.title}")
    except IndexError:
        print("Error: Invalid task index.")


def list_tasks(task_list):
    """
    Displays all tasks with status and overdue indication.
    """

    if not task_list:
        print("No tasks available.")
        return

    print("\n===== TASK LIST =====")

    today = date.today()

    for i, task in enumerate(task_list):
        status = "X" if task.completed else "-"

        due_text = "No due date"
        overdue_text = ""

        if task.due_date:
            due_text = task.due_date.strftime("%Y-%m-%d")

            if not task.completed and task.due_date < today:
                overdue_text = " (OVERDUE)"

        print(
            f"{i}: [{status}] "
            f"{task.title} | Due: {due_text}{overdue_text}"
        )