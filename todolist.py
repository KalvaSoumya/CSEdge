class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))
        print("Task added successfully!")

    def delete_task(self, index):
        try:
            del self.tasks[index]
            print("Task deleted successfully!")
        except IndexError:
            print("Task index out of range!")

    def mark_as_completed(self, index):
        try:
            self.tasks[index].completed = True
            print("Task marked as completed!")
        except IndexError:
            print("Task index out of range!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for i, task in enumerate(self.tasks):
                status = "Completed" if task.completed else "Pending"
                print(f"{i + 1}. [{status}] {task.description}")

def main():
    task_manager = TaskManager()

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            task_manager.add_task(description)
        elif choice == "2":
            index = int(input("Enter task index to delete: ")) - 1
            task_manager.delete_task(index)
        elif choice == "3":
            index = int(input("Enter task index to mark as completed: ")) - 1
            task_manager.mark_as_completed(index)
        elif choice == "4":
            task_manager.display_tasks()
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()