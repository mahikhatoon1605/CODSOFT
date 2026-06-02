import json
import os

FILE_NAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except:
                return []
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n--- TASK LIST ---")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")

def complete_task(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number to complete: "))
        tasks[task_no - 1]["completed"] = True
        save_tasks(tasks)
        print("Task completed!")
    except:
        print("Invalid input.")

def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number to delete: "))
        deleted = tasks.pop(task_no - 1)
        save_tasks(tasks)
        print(f"Deleted: {deleted['task']}")
    except:
        print("Invalid input.")

def update_task(tasks):
    view_tasks(tasks)

    try:
        task_no = int(input("Enter task number to update: "))
        new_task = input("Enter updated task: ")

        tasks[task_no - 1]["task"] = new_task

        save_tasks(tasks)
        print("Task updated!")
    except:
        print("Invalid input.")

def main():
    tasks = load_tasks()

    while True:
        print("\n========== TO-DO LIST ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            update_task(tasks)

        elif choice == "4":
            complete_task(tasks)

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()