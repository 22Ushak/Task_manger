# task_management_app.py

def display_tasks(tasks):
    """Display all tasks in the list. If no tasks, print a message indicating that."""
    if tasks:
        print(f"Total tasks: {tasks}")
    else:
        print("No tasks available.")

def add_task(tasks):
    """Prompt the user to add a new task with input validation to prevent duplicates."""
    new_task = input("Enter the task you want to add: ").strip()  # Remove extra spaces
    if new_task:
        if new_task not in tasks:
            tasks.append(new_task)  # Add task if it's not a duplicate
            print(f"Task '{new_task}' has been successfully added.")
        else:
            print("This task already exists.")
    else:
        print("Task cannot be empty.")

def update_task(tasks):
    """Allow the user to update an existing task."""
    updated_val = input("Enter the task name you want to update: ").strip()
    if updated_val in tasks:
        new_task = input("Enter the new task: ").strip()  # Get the new task name
        if new_task:
            ind = tasks.index(updated_val)  # Find the index of the old task
            tasks[ind] = new_task  # Replace with the new task
            print(f"Updated task '{updated_val}' to '{new_task}'.")
        else:
            print("New task cannot be empty.")
    else:
        print("Task not found.")

def delete_task(tasks):
    """Delete a task from the list based on user input."""
    del_val = input("Which task do you want to delete: ").strip()
    if del_val in tasks:
        tasks.remove(del_val)  # Remove the specified task
        print(f"Task '{del_val}' has been deleted.")
    else:
        print("Task not found.")

def task_management_app():
    """Main function to run the task management application."""
    tasks = []  # Initialize an empty task list
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    # Add initial tasks based on user input
    total_task = int(input("Enter how many tasks you want to add: "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ").strip()  # Prompt for task name
        if task_name and task_name not in tasks:
            tasks.append(task_name)  # Add valid task to the list
        elif not task_name:
            # Re-prompt if the task name is empty
            print("Task cannot be empty.")
            task_name = input(f"Enter task {i}: ").strip()
        else:
            print("This task already exists.")
        if task_name and task_name not in tasks:
            tasks.append(task_name)  # Add the task after re-validation

    # Main loop for task operations
    while True:
        try:
            # Display options and get user input
            operation = int(input(
                "\nEnter:\n1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit/Stop\n"
            ))

            if operation == 1:
                add_task(tasks)  # Add a new task
            elif operation == 2:
                update_task(tasks)  # Update an existing task
            elif operation == 3:
                delete_task(tasks)  # Delete a task
            elif operation == 4:
                display_tasks(tasks)  # View all tasks
            elif operation == 5:
                # Confirm before exiting
                confirm_exit = input("Are you sure you want to exit? (y/n): ").lower()
                if confirm_exit == 'y':
                    print("Closing the program....")
                    break  # Exit the program
            else:
                print("Invalid input. Please enter a number from 1 to 5.")
        except ValueError:
            # Handle non-integer input gracefully
            print("Invalid input. Please enter a valid number.")

# Run the application
if __name__ == "__main__":
    task_management_app()
