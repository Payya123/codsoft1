class Task:
    def __init__(self, description, status="Pending"):
        self.description = description
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __repr__(self):
        return f"{self.description} - {self.status}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def update_task_status(self, index, new_status):
        self.tasks[index].update_status(new_status)

    def __repr__(self):
        return "\n".join([f"{index + 1}. {task}" for index, task in enumerate(self.tasks)])

def main():
    todo_list = TodoList()

    while True:
        print("\n===== To-Do List =====")
        print(todo_list)
        print("=======================")

        print("\n1. Add task\n2. Mark task as done\n3. Update task\n4. Quit\n")

        choice = input("Choose an option: ")

        if choice == "1":
            task_description = input("Enter task description: ")
            todo_list.add_task(task_description)
        elif choice == "2":
            index = int(input("Enter task number to mark as done: ")) - 1
            todo_list.update_task_status(index, "Done")
        elif choice == "3":
            index = int(input("Enter task number to update: ")) - 1
            new_status = input("Enter new status (Pending/Done): ")
            todo_list.update_task_status(index, new_status)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose again.")

    print("Thank you for using the To-Do List!")

if __name__ == "__main__":
    main()
