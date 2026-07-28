class Task:
    def __init__(self, title):
        self.title = title
        self.is_done = False

    def toggle_done(self):
        self.is_done = not self.is_done

    def __str__(self):
        status = "DONE" if self.is_done else "Pending"
        return f"{self.title} [{status}]"


class TodoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        title = input("Please Fill your Task: ").strip()
        if title:
            self.tasks.append(Task(title))
            print(f"Task '{title}' added successfully!")
        else:
            print("Task cannot be empty.")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return

        print("\nYour Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}- {task}")

    def update_task(self):
        self.read_tasks()
        if not self.tasks:
            return

        idx = int(input("Enter task number to update: ")) - 1
        if 0 <= idx < len(self.tasks):
            new_title = input("Enter new task name: ").strip()
            if new_title:
                self.tasks[idx].title = new_title
                print("Task updated.")

    def delete_task(self):
        self.read_tasks()
        if not self.tasks:
            return

        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(self.tasks):
            removed = self.tasks.pop(idx)
            print(f"Deleted task: {removed.title}")

    def toggle_task_status(self):
        self.read_tasks()
        if not self.tasks:
            return

        idx = int(input("Enter task number to toggle status: ")) - 1
        if 0 <= idx < len(self.tasks):
            task = self.tasks[idx]
            task.toggle_done()
            new_status = "DONE" if task.is_done else "Pending"
            print(f"Task status changed to [{new_status}].")

    def run(self):
        while True:
            print("\n 1. Add Task\n 2. View Tasks\n 3. Update Task\n 4. Delete Task\n 5. Toggle Task Status\n 6. Exit")
            choice = input("Select option: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.read_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.toggle_task_status()
            elif choice == "6":
                break


if __name__ == "__main__":
    app = TodoApp()
    app.run()