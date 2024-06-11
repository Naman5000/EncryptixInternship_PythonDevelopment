class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added task: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid task number.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. View tasks")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_number_input = input("Enter the task number to remove: ")
            if task_number_input.isdigit():
                task_number = int(task_number_input)
                todo_list.remove_task(task_number)
            else:
                print("Invalid input. Please enter a valid task number.")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
