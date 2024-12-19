from ToDoFunctionality import add_task, view_task, delete_task
def show_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Thank you for using this To-Do list!")
            break
        else:
            print("Invalid option. Please try again")

if __name__ == "__main__":
    main()