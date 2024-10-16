# To-Do List Application

tasks = []

def display_tasks():
    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(task):
    tasks.append(task)
    print(f'"{task}" has been added to your To-Do list.')

def delete_task(index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f'"{removed_task}" has been removed from your To-Do list.')
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            try:
                task_number = int(input("Enter the task number to delete: ")) - 1
                delete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
