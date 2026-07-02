import json
import os

class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Loads tasks from the JSON file."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError):
            return []

    def save_tasks(self):
        """Saves current tasks to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title):
        task_id = len(self.tasks) + 1
        new_task = {"id": task_id, "title": title, "completed": False}
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def delete_task(self, task_id):
        self.tasks = [t for t in self.tasks if t['id'] != task_id]
        # Re-index IDs to keep them sequential
        for index, task in enumerate(self.tasks):
            task['id'] = index + 1
        self.save_tasks()
        print(f"Task {task_id} deleted.")

    def mark_completed(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} marked as completed.")
                return
        print("Task not found.")

    def update_task(self, task_id, new_title):
        for task in self.tasks:
            if task['id'] == task_id:
                task['title'] = new_title
                self.save_tasks()
                print(f"Task {task_id} updated.")
                return
        print("Task not found.")

    def view_tasks(self):
        if not self.tasks:
            print("\nYour list is empty.")
            return
        print("\n--- Current Tasks ---")
        for t in self.tasks:
            status = "[x]" if t['completed'] else "[ ]"
            print(f"{t['id']}. {status} {t['title']}")

def main():
    todo = TodoList()
    
    while True:
        print("\n--- To-Do Menu ---")
        print("1. View Tasks\n2. Add Task\n3. Update Task\n4. Delete Task\n5. Mark Completed\n6. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            todo.view_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            todo.add_task(title)
        elif choice == '3':
            try:
                tid = int(input("Enter task ID to update: "))
                new_title = input("Enter new title: ")
                todo.update_task(tid, new_title)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            try:
                tid = int(input("Enter task ID to delete: "))
                todo.delete_task(tid)
            except ValueError:
                print("Invalid input.")
        elif choice == '5':
            try:
                tid = int(input("Enter task ID to complete: "))
                todo.mark_completed(tid)
            except ValueError:
                print("Invalid input.")
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()