'''
Activity 4.2: Interactive To-Do List (using List Operations)
○ Format: Individual coding challenge.
○ Instructions: Students will implement a very basic text-based to-do list manager using
what they&#39;ve learned about lists.
○ Features to include (minimum):
■ An empty list todo_list initially.
■ A while loop that presents a menu:
1. Add a task
2. View tasks
3. Mark task as complete (remove by index or name)
4. Exit
■ Use input() to get user choices.
■ Use list methods (append(), remove() or pop(), len()) to manage the todo_list.
○ Purpose: Practical application of list operations in a mini-project context, integrating
loops and conditionals.
'''

todo_list = []
options = ["Add a task", "View tasks", "Mark task as complete", "Exit"]
choice = 0
while choice != 4:
    print("\nTo-Do List Manager")
    i = 1
    for o in options:
        print(f"{i}.{o}")
        i+=1
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f"Task '{task}' added.")
        print(f"\nYour todo list: {todo_list}")
    elif choice == 2:
        if todo_list:
            print(f"\nYour todo list: {todo_list}")
            print("Your tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}.{task}")
        else:
            print("Your to-do list is empty.")
    elif choice == 3:
        if todo_list:
            print(f"\nYour todo list: {todo_list}")
            print("Your tasks:")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
            try:
                task_index = int(input("Enter the number of the task to mark as complete: ")) - 1
                if 0 <= task_index < len(todo_list):
                    completed_task = todo_list.pop(task_index)
                    print(f"Task '{completed_task}' marked as complete.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Your to-do list is empty.")
