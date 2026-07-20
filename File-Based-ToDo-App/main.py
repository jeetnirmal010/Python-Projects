def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task.capitalize() + "\n")
    print("Task Saved Successfully!")


def view_tasks():
    with open("tasks.txt", "r") as file:
        print("\n===== YOUR TASKS =====")
        print(file.read())


while True:
    print("\n====== TO-DO APP ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice! Please try again.")