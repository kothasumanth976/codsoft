class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task is added: '{task}'")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return

        print("\nYour To-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")


def main():
    todo = ToDoList()

    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            task = input("Enter the task: ").strip()
            todo.add_task(task)

        elif choice == "2":
            todo.view_tasks()

        elif choice == "4":
            print("Exiting To-Do List. Bye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
