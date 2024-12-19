
# Taking user input and adding it to the end of a list
def add_task(tasks):
    task = input("Enter a task to your todo list: ")
    tasks.append(task)
    print(f'Task "{task}" added. ')

# The viewing task fuction
def view_task(tasks):
    #Checks to see there is item in list
    if len(tasks) == 0:
        print("Your To-Do list is empty. ")
    else:
        '''
        x and task are temporary variables goes through tasks list enumrating the list and
        combining the tasks list with the number starting at 1
        '''
        print("\nYour To-Do List: ")
        for x, task in enumerate(tasks, 1):
            print(f"{x}. {task}")

def delete_task(tasks):
    """Function to delete a task from the tasks list"""
    view_task(tasks)  # Show tasks before deleting
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                deleted_task = tasks.pop(task_num - 1)
                print(f'Task "{deleted_task}" deleted.')
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")