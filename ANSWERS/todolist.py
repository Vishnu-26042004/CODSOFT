import json

TODO_FILE = "todo_list.json"

def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task_desc):
    tasks = load_tasks()
    tasks.append({"task": task_desc, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found!")
        return
    
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['task']}")

def mark_task_completed(task_number):
    """Mark a task as completed."""
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        save_tasks(tasks)
        print("Task deleted successfully!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task_desc = input("Enter task description: ")
            add_task(task_desc)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                mark_task_completed(task_number)
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == "4":
            view_tasks()
            try:
                task_number = int(input("Enter task number to delete: "))
                delete_task(task_number)
            except ValueError:
                print("Invalid input. Enter a number.")
        elif choice == "5":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()