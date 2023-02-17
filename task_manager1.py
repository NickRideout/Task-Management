# =====Importing Libraries===========

from datetime import date
from datetime import datetime
import os.path


# =====Defining Functions===========


def reg_user():
  # Checking if the input_name is not equal to "admin"
    if input_name != "admin":
        print("\nOnly admins can create new users, please select a different option.\n")

    else:
      # The below code is opening the user.txt file and appending the user's input to the file.
        with open('user.txt', 'a+') as open_user_file:
            open_user_file.seek(0)  
            user_file_content = open_user_file.read()
            new_username = input("Create a new username: ")
           # Checking if the username is already in the file.
            while new_username in user_file_content:
                new_username = input("\nThis username is taken. Please enter another username: \n")

            new_password = input("Create a password: ")
            password_check = input("Please confirm your password: ")

          # The below code is checking if the new password is the same as the password check.
            if new_password != password_check:
                password_check = input("Your passwords don't match, please re-enter your password: ")

            # Writing the new username and password to the user_file.txt file.
            open_user_file.write(f"\n{new_username}, {new_password}")

            print('\n User created, thanks! \n')



def add_task():

    assignee = input("\nEnter the assignee's username: ")

    # Checking if the assignee is in the user_names list.
    if assignee not in user_names:
        assignee = input("\nThis username is not in the system, please enter a known user or create a new user: \n")
    else:
        pass

    task = str(input("Enter your task: "))

    task_description = str(input("Enter your task description: "))

    date_due = str(input("Enter the task due date (e.g. 10 October 2023): "))

    # The below code is creating a variable called current_date and assigning it the value of the
    # date.today() function.
    current_date = date.today()
    # Converting the date to a string.
    current_date = current_date.strftime("%d %B %Y")

    task_status = 'No'

    with open('tasks.txt', 'a+') as addto_task_file:
        addto_task_file.write(f"\n{assignee}, {task}, {task_description}, {date_due}, {current_date}, {task_status}")


def view_all():


    task_num = 1
   # The below code is opening the file tasks.txt in read mode and assigning it to the variable
   # read_tasks_file.
    with open('tasks.txt', 'r') as read_tasks_file:
        for line in read_tasks_file:
            rtf_line = line.split(", ")
            print(f"""
        -------------------[Task: {task_num}]--------------------
        Task:               {rtf_line[1]}
        Assigned to:        {rtf_line[0]}
        Date assigned:      {rtf_line[4]}
        Due date:           {rtf_line[3]}
        Task complete?      {rtf_line[-1]}
        Task description:   
            {rtf_line[2]}
        -----------------------------------------------\n""")
            task_num += 1


def view_mine():

    task_num = 0
 # Creating an empty list called my_tasks.
    my_tasks = []
    # Opening the file and reading it.
    with open('tasks.txt', 'r') as read_tasks_file:
        print("\n=== MY TASKS ===")
        for line in read_tasks_file:
            rtf_line = line.split(", ")
            if input_name == rtf_line[0]:
                my_tasks.append(rtf_line)
                print(f"""
-------------------[Task: {task_num + 1}]---------------------
    Task:               {rtf_line[1]}
    Assigned to:        {rtf_line[0]}
    Date assigned:      {rtf_line[4]}
    Due date:           {rtf_line[3]}
    Task complete?      {rtf_line[-1]}
    Task description:   
        {rtf_line[2]}
-----------------------------------------------\n""")
                task_num += 1

    # The below code is counting the number of items in the list my_tasks.
    num_my_tasks = len(my_tasks)


   # Asking the user to input a number between 1 and 4.
    menu = int(input('''\nWould you like to:
    1  - Mark a task as complete
    2  - Edit a task assignee
    3  - Edit a task due date
    4  - Return to main menu
    : '''))

    if menu == 4:
        menu_selector()  

    else:
     
       # Asking the user to input a number between 1 and 4. If the user inputs a number outside of
       # that range, it will ask the user to input a number between 1 and 4 again.
        while menu not in [1, 2, 3, 4]: 
            menu = int(input("Option not in menu. Please select another option: \n"))
        # Asking the user to select a task number.
        user_selection = int(input("Select a task number: \n"))  
        edited_tasks_content = ''  

       # Asking the user to select a task number.
        while user_selection not in range(num_my_tasks + 1):  
            user_selection = int(input("Task number does not exist. Please select a valid task number: \n"))

        # Opening the file in read mode.
        if menu == 1:  
            r_tasks_file = open('tasks.txt', 'r')
           
            # Splitting the line into a list of strings.
            for line in r_tasks_file:
                split_line = line.split(', ')

                if split_line == my_tasks[user_selection - 1]:
                    split_line[-1] = "Yes" + "\n" 
                split_line = ', '.join(split_line)  
                edited_tasks_content += split_line  
            with open('tasks.txt', 'w+') as write_tasks_file:
                write_tasks_file.write(edited_tasks_content)  
            print("\n✨ Saved as complete. ✨ \n")

       # Opening the file in read mode.
        elif menu == 2:  
            r_tasks_file = open('tasks.txt', 'r')
           # Checking if the last item in the list is 'Yes'
            for line in r_tasks_file:
                split_line = line.split(', ')
                if split_line == my_tasks[user_selection - 1]:
                    if 'Yes' in split_line[-1]:
                        print(
                            "This task is already complete, you can't change the assignee.\n Choose another option from the menu:")
                        menu_selector()
                    # Checking if the language is Python or not. If it is not Python, then it will
                    # execute the code in the else block.
                    else:
                        new_assignee = str(input("Enter the new assignee: \n")).lower()
                        split_line[0] = new_assignee
                split_line = ', '.join(split_line) 
                edited_tasks_content += split_line  
           # Opening the file and writing the edited content to the file.
            with open('tasks.txt', 'w+') as write_tasks_file:
                write_tasks_file.write(edited_tasks_content)  
            print("\n✨ Assignee change. ✨ \n")
            r_tasks_file.close()

       # Opening the file in read mode.
        elif menu == 3:  
            r_tasks_file = open('tasks.txt', 'r')
            for line in r_tasks_file:
                split_line = line.split(', ')
                # Checking if the task is already complete. If it is, it will not allow the user to
                # edit it.
                if split_line == my_tasks[user_selection - 1]:
                    if 'Yes' in split_line[-1]:
                        print(
                            "This task is already complete, you can't edit it.\n Choose another option from the menu:")
                        menu_selector()
                   # The below code is checking if the user is using Python 2 or Python 3. If the user
                   # is using Python 2, the code will ask the user to enter the new due date. If the
                   # user is using Python 3, the code will ask the user to enter the new due date.
                    else:
                        new_due_date = input("Enter the new due date (e.g. 10 January 2023): \n")
                        split_line[-3] = new_due_date
                split_line = ', '.join(split_line) 
                edited_tasks_content += split_line  
            with open('tasks.txt', 'w+') as write_tasks_file:
                write_tasks_file.write(edited_tasks_content)  
            print("\n✨ Due date changed. ✨ \n")


def view_stats():

    
  
  # Checking if the files exist.
    if os.path.exists('task_overview.txt') and os.path.exists(
            'user_overview.txt'):  
        if os.stat("task_overview.txt").st_size == 0: 
            generate_reports()
    else:
        generate_reports() 

  # Reading the file and storing the content in a variable.
    with open('task_overview.txt', 'r') as read_t_f:
        task_content = read_t_f.readlines()
        for line in task_content:
            line = line.replace('\n', '')
            print(line)

 # Opening the file and reading the lines.
    with open('user_overview.txt', 'r') as read_u_f:
        user_content = read_u_f.readlines()
        for line in user_content:
            line = line.replace('\n', '')
            print(line)


def menu_selector():
  # Checking if the input_name is equal to admin.
    while True:
        if input_name == 'admin':
          
            menu = input('''\n=== MAIN MENU ===
Select one of the following options:
         
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate report
    ds - Display stats 
    e - Exit
    : ''').lower()

        else:
            
            menu = input('''\n=== MAIN MENU ===
Select one of the following options:
            
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    e - Exit
    : ''').lower()

       # The below code is a menu for the user to choose from.
        if menu == 'r':
          
            reg_user()

        elif menu == 'a':
           
            add_task()

        elif menu == 'va':
            
            view_all()

        elif menu == 'vm':
           
            view_mine()

        elif menu == 'e':
            print('Goodbye!')
            exit()

        elif menu == 'ds':
            
            view_stats()

        elif menu == 'gr':
            generate_reports()
            

        else:
            print("You have made a wrong choice, Please try again")


def generate_reports():
    

    
    with open('tasks.txt', 'r') as read_tasks_file:
        tasks_file_content = read_tasks_file.readlines()

   
    # The below code is counting the number of lines in the file.
    total_tasks = len(tasks_file_content)

    
    # The below code is using the date module to get the current date and then formatting it to the
    # format of dd Month YYYY.
    current_date = date.today().strftime("%d %B %Y")

    
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0

   
   # The below code is iterating through the tasks_file_content and splitting each line by the comma.
   # It then checks if the last item in the list is 'Yes' and if it is, it adds 1 to the
   # completed_tasks variable.
    for line in tasks_file_content:
        split_line = line.split(', ')
        if 'Yes' in split_line[-1]:
            completed_tasks += 1
        else:
            uncompleted_tasks += 1
            task_due_date = split_line[-3]
            
            obj_current_date = datetime.strptime(current_date, "%d %B %Y")
            obj_task_due_date = datetime.strptime(task_due_date, "%d %b %Y")
            if obj_task_due_date < obj_current_date:
                overdue_tasks += 1

    
    
    with open('task_overview.txt', 'w+') as write_task_overview_file:
        write_task_overview_file.write(f""" 
            -----------------------------------------------
                TASK OVERVIEW REPORT: {current_date}
        
                Total tasks:        | {total_tasks}
                    Completed:      | {completed_tasks}
                    Incomplete:     | {uncompleted_tasks}
                    Overdue:        | {overdue_tasks}
                    % Incomplete:   | {int((uncompleted_tasks / total_tasks) * 100)}%
                    % Overdue:      | {int((overdue_tasks / total_tasks) * 100)}%
        
            -----------------------------------------------
                """)

   

    # Opening the file user.txt and reading the lines.
    with open('user.txt', 'r') as read_user_file:
        users = read_user_file.readlines()

        
        # Creating an empty list called all_users.
        all_users = []

        # Splitting the line by the comma and space.
        for line in users:
            split_line = line.split(', ')  

            if split_line[0] not in all_users:
                all_users.append(split_line[0])
            else:
                pass

     # The below code is counting the number of users in the list.
        total_users = len(all_users)

        write_user_overview_file = open('user_overview.txt', 'w+')
        new_file_content = (f""" 
            -----------------------------------------------
                USER OVERVIEW REPORT: {current_date}
        
                Total users:        | {total_users}
                Total tasks:        | {total_tasks}
                
                USER DETAILS:""")

    

   # The below code is converting the string current_date into a datetime object.
    obj_current_date = datetime.strptime(current_date, "%d %B %Y")

    # Opening the file 'tasks.txt' in read mode.
    read_tasks_file = open('tasks.txt', 'r')

   # Creating an empty dictionary.
    user_stats_dict = {} 

    # Creating a dictionary with the keys being the users and the values being a dictionary with the
    # keys being the stats and the values being 0.
    for user in all_users:  
        user_stats_dict[user] = {'Total tasks': 0,
                                 'Complete tasks': 0,
                                 'Incomplete tasks': 0,
                                 'Overdue tasks': 0,
                                 '% Complete': 0,
                                 '% Incomplete': 0,
                                 '% Overdue': 0, }


    for line in read_tasks_file:  
        split_line = line.split(', ')
        current_user = split_line[0]
        user_stats_dict[current_user]['Total tasks'] += 1  
        if 'No' in split_line[-1]:  
            user_stats_dict[current_user][
                'Incomplete tasks'] += 1  
            task_due_date = split_line[-3]  
            obj_task_due_date = datetime.strptime(task_due_date, "%d %b %Y")
            if obj_task_due_date < obj_current_date:
                user_stats_dict[current_user]['Overdue tasks'] += 1  
        elif 'Yes' in split_line[-1]:
            user_stats_dict[current_user]['Complete tasks'] += 1  

    for user in all_users:  
        # Calculating the percentage of completed tasks for each user.
        try:
            user_stats_dict[user]['% Complete'] = int(
                user_stats_dict[user]['Complete tasks'] / user_stats_dict[user]['Total tasks'] * 100)
        except ZeroDivisionError:
            user_stats_dict[user]['% Complete'] = 0

       # Calculating the percentage of incomplete tasks for each user.
        try:
            user_stats_dict[user]['% Incomplete'] = int(
                user_stats_dict[user]['Incomplete tasks'] / user_stats_dict[user]['Total tasks'] * 100)
        except ZeroDivisionError:
            user_stats_dict[user]['% Incomplete'] = 0

      # Calculating the percentage of overdue tasks for each user.
        try:
            user_stats_dict[user]['% Overdue'] = int(
                user_stats_dict[user]['Overdue tasks'] / user_stats_dict[user]['Total tasks'] * 100)
        except ZeroDivisionError:
            user_stats_dict[user]['% Overdue'] = 0

    for user in user_stats_dict:  
        new_file_content += (f"""
        
        USER: {user}
        
        Total Tasks:                | {user_stats_dict[user]['Total tasks']}
            % of All Tasks:         | {int(user_stats_dict[user]['Total tasks'] / total_tasks * 100)}%
                
            Complete Tasks:         | {user_stats_dict[user]['Complete tasks']}
                % Complete:         | {user_stats_dict[user]['% Complete']}%
            Incomplete Tasks:       | {user_stats_dict[user]['Incomplete tasks']}
                % Incomplete:       | {user_stats_dict[user]['% Incomplete']}%
            Overdue Tasks:          | {user_stats_dict[user]['Overdue tasks']}
                % Overdue Tasks:    | {user_stats_dict[user]['% Overdue']}%
                    
        -----------------------------------------------""")

    read_tasks_file.close()

    with open('user_overview.txt', 'w+'):  
        write_user_overview_file.write(new_file_content)

    print(f"\n✨ Report generated, please see text files. ✨\n")


# ====Login Section====


# The below code is asking the user to input their username and password.
print("\n==== WELCOME TO YOUR TASK MANAGER ====\n")
input_name = input("Enter your username: ")
input_password = input("Enter your password: ")



# Opening the file user.txt and reading the content of the file.
with open('user.txt', 'r') as read_user_file:
    all_user_file_content = read_user_file.read()

# Taking the content of the file and splitting it into a list.
list_login_details = all_user_file_content.split()
for i in range(len(list_login_details)):
    list_login_details[i] = list_login_details[i].replace(',', '')


# Creating two empty lists, and two empty strings.
user_names = []
passwords = []
name1 = ""
password1 = ""


while True:
   # Taking the first two elements of the list and appending them to the user_names and passwords
   # lists.
    if len(list_login_details) > 0:
        name1 = list_login_details.pop(0)
        user_names.append(name1)
        password1 = list_login_details.pop(0)
        passwords.append(password1)
    else:
        break



# Setting the index of the username and password to 0.
username_index = 0
password_index = 0

while True:
   # Checking if the input name is in the list of user names.
    if input_name in user_names:
        username_index = user_names.index(input_name)
        pass
    else:
     # Asking the user to re-enter the username if it is incorrect.
        input_name = input("Incorrect username, please re-enter: ")
        continue
 # Checking if the input_password is in the passwords list.
    if input_password in passwords:
        password_index = passwords.index(input_password)
        pass
    else:
 # Asking the user to re-enter the password if the password is incorrect.
        input_password = input("Incorrect password, please re-enter: ")
        continue
   # Checking if the username and password are correct.
    if user_names[username_index] == input_name and passwords[password_index] == input_password:
        print(f"\n✨ Login details correct. Welcome {input_name}! ✨\n")
        break
   # Asking the user to enter a password. If the password is correct, it will print "Welcome". If the
   # password is incorrect, it will ask the user to re-enter the password.
    else:
        input_password = input("Incorrect password, please re-enter: ")
        continue

# Calling the function menu_selector()
menu_selector()