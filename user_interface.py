# Create a command-line interface for the user to interact with the program

print("Welcome to the To-Do List App!")
print("In just a few steps, you will have your to-do list ready to go!")
print("Let's get started!")

import os

tasks = []


#--------------Creating functions for the menu options----------------

def clear(): # This function will clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def add_task(): # This function will allow the user to add a task to the list
    task = input('Please enter a task you would like to add: ')
    tasks.append(task)
    print(f'Okay, I have added "{task}" to your to-do list.')

def view_tasks(): # This function will print the list of tasks
    
    if len(tasks) == 0:
        print("You don't have any tasks in your to-do list at this time.")
    else:
        print('Here are your tasks:') 
        for task in tasks: 
            
            print(tasks.index(task) +1, end=' ') # This code will populate the list of tasks with numbers in front of each task based on the index of the task in the list +1 
            print(' ', task)
            
def updated_tasks(): # This function will print the updated list of tasks after a task has been marked as complete or deleted
    print('Here is your updated tasks list:')
    for task in tasks: 
        print(tasks.index(task) +1, end=' ')
        print(' ', task)
            
   
def mark_complete(): # This function will allow the user to mark a task as complete
    view_tasks()
    try:
        task_to_mark = int(input('Please enter the task you would like to mark as complete: (select by number) '))
        task_to_mark = task_to_mark - 1
        tasks[task_to_mark] = tasks[task_to_mark] + ' (complete)'
    except ValueError:
        print('Please enter a valid number.')
    except IndexError:
        print('Please enter a number within the available list parameters.')
    else:
        print(f'Great! You have marked "{tasks[task_to_mark]}".')

def delete_task(): # This function will allow the user to delete a task
    view_tasks()
    try:
        task_to_delete = int(input('Please enter the task you would like to delete: (select by number) '))
        task_to_delete = task_to_delete - 1
        deleted_task = tasks.pop(task_to_delete)
    except ValueError:
        print('Please enter a valid number.')
    except IndexError:
        print('Please enter a number within the available list parameters.')
    else:
        print(f'You have deleted "{deleted_task}" from your to-do list.')

def quit_app(): # This function will allow the user to quit the app
    print('Thank you for using the To-Do List App! Have a great day!')
    exit()
    

#-----------------Creating the main loop----------------

while True:
    try:
        user_choice = int(input('''

        Main Menu:
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit 
Please select a main menu option:(choose number) '''))
        if user_choice == 1:
            clear()
            add_task()
        elif user_choice == 2:
            clear()
            view_tasks()
        elif user_choice == 3:
            clear()
            mark_complete()
            updated_tasks()
        elif user_choice == 4:
            clear()
            delete_task()
            updated_tasks()
        elif user_choice == 5:
            clear()
            quit_app()
        else:
            print('Please enter a valid menu option.')

    except ValueError:
        print('Please enter a valid number.')
    except Exception as e:
        print(f"An error occurred: {e}")

