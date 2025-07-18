tasks = []

while True:
    choice = input("Add/View/Exit: ").lower()
    if choice == "add":
        task = input("Enter task: ")
        tasks.append(task)
    elif choice == "view":
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "exit":
        break
