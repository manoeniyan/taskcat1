tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. Add Task  2. Show Tasks  3. Remove Task  4. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == '2':
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == '3':
        idx = int(input("Enter task number to remove: ")) - 1
        if 0 <= idx < len(tasks):
            tasks.pop(idx)
            print("Task removed!")
    elif choice == '4':
        break
