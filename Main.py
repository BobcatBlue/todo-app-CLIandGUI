#  DAY 1

# print something to the screen/user:
# print("Enter a to-do:")

# get input:
# input()

# save the users input to a variable:

# user_text = input("Enter a to-do:")
# print(user_text)

# ^^^ functions can return a value
# Text information is known as a STRING, always shown as text in quotes

# You can name variables whatever you want, but you cannot have numbers at the beginning of the variable name.

# prompt = "Enter a to-do:"
# user_text = input(prompt)
# print(user_text)


# -----------------------
#  STORING USER INPUT
#     the LIST f(x)
# ------------------------

"""
prompt = "Enter a to-do:"

todo1 = input(prompt)
todo2 = input(prompt)
todo3 = input(prompt)

#List syntax:
#************************************
todos = [todo1, todo2, todo3, "Hello"]

#lists always use square brackets []
#**************************************

print(todos)
print(type(todo1))
"""
###################################################################################################################


# ******************************************
# ******************************************
#                DAY 2
#         While-Loop  & Methods
# ******************************************
# ******************************************


"""
prompt = "Enter a to-do: "

while True:
    todo = input(prompt)
    todos = [todo]
    print(todos)
"""
# ^^^^  So, this code won't work for us because every time the user inputs a new list item,
#       the new entry overwrites the previous one and doesn't keep track of all the times,
################################################
"""
prompt = "Enter a to-do:"

todos = []

while True:
    todo = input(prompt)
    todos.append(todo.capitalize())
    print(todos)
"""

# ^^^   To fix that problem, we'll start by defining todos as a blank list and then using the .append method
#       to append each user-inputted string into a new variable stored within the list.
#       The .append syntax is called a METHOD
######################################################################################################################


# *************************************
# *************************************
#               Day 3
#       Match-Case & For Loops
# *************************************
# *************************************

"""
In this lesson, we'll allow the program to take decisions; make it more intelligent.
User can add items to the to-do list, or display the list when the user wants to see it.
"""

"""
todos = []

while True:
    user_action = input("Type add, show, or exit:  ")
    user_action = user_action.lower()

    match user_action:
        case 'add':
            todo = input("Enter a task:  ")
            todos.append(todo)
        case 'show':
            print(todos)
        case 'exit':
            break

print("Bye!")
"""

########################
#  Using the FOR loop
########################
"""
todos = []

while True:
    user_action = input("Type add, show, or exit:  ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task:  ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print(item)
        case 'exit':
            break

print("Bye!")
"""

# ***************************************
# ***************************************
#                Day 4
#   Type-conversion and List Indexing
# ***************************************
# ***************************************
"""
todos = []

while True:
    user_action = input("Type add, show, edit, or exit:  ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task:  ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                print(index + 1, item)
        case 'edit':
            number = int(input("Which item number would you like to edit?: "))
            number = number - 1
            new_todo = input("Enter a new item: ")
            todos[number] = new_todo
        case 'exit':
            break

print("Bye!")
"""

# ***************************************
# ***************************************
#                Day 5
#      Enumeration and F-Strings
#       also, .pop(), .remove(), .clear()
# ***************************************
# ***************************************
"""
todos = []

while True:
    user_action = input("Type add, show, edit, complete, or exit:  ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task:  ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                index = index + 1
                row = f"{index}-{item}"
                print(row)
        case 'edit':
            number = int(input("Which item number would you like to edit?: "))
            number = number - 1
            new_todo = input("Enter a new item: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Which item number is complete?: "))
            number = number - 1
            todos.pop(number)
        case 'exit':
            break

print("Bye!")
"""

# ***************************************
# ***************************************
#                Day 6
#      Storing Items in Text Files
#   ----------------------------------
# text files, read, write, write lines, read lines
# ***************************************
# ***************************************

"""
while True:
    user_action = input("Type add, show, edit, complete, or exit:  ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task:  ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Which item number would you like to edit?: "))
            number = number - 1
            new_todo = input("Enter a new item: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Which item number is complete?: "))
            number = number - 1

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.pop(number)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'exit':
            break

print("\n" + "Bye!")
"""

# ***************************************
# ***************************************

#                Day 7
#     Improving the Program Output:
#           -------------
#    List Comprehensions & Comments

# ***************************************
# ***************************************
"""
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete, or exit:  ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task:  ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()

            new_todos = [item.strip('\n') for item in todos]        # List Comprehension
                                                                    # Used instead of a for-loop to remove the extra
                                                                    # break-line between items when the list is shown

            for index, item in enumerate(new_todos):
                # item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Which item number would you like to edit?: "))
            number = number - 1
            new_todo = input("Enter a new task: ") + "\n"

            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()

            todos[number] = new_todo

            file = open("todos.txt",'w')
            file.writelines(todos)
            file.close()

        case 'complete':
            number = int(input("Which item number is complete?: "))
            number = number - 1

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.pop(number)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'exit':
            break

print("\n" + "Bye!")
"""

# ***************************************
# ***************************************

#                Day 8
#     Improving the Program Output:
#           -------------
#    List Comprehensions & Comments

# ***************************************
# ***************************************

# Today is a day where we focus not on improving the program's output, but we improve the code itself.
# We'll make the code more readable and efficient, starting with how we open and close files
# Right now we use the open() and close() functions, but this can be done better with a  With-Context-Manager
"""
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete, or exit:  ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a task:  ") + "\n"

            with open("todos.txt",'r') as file:                     # With-context-manager
                todos = file.readlines()

            todos.append(todo)

            with open("todos.txt", 'w') as file:                    # with-context-manager
                file.writelines(todos)

        case 'show':
            file = open("todos.txt", 'r')
            todos = file.readlines()
            file.close()

            new_todos = [item.strip('\n') for item in todos]        # List Comprehension
                                                                    # Used instead of a for-loop to remove the extra
                                                                    # break-line between items when the list is shown

            for index, item in enumerate(new_todos):
                # item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Which item number would you like to edit?: "))
            number = number - 1

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new task: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Which item number is complete?: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

            message = f"\n'{completed_todo}' was removed from the list!\n"
            print(message)

        case 'exit':
            break

print("\n" + "Bye!")
"""

# ***************************************
# ***************************************
#             Days 9 & 10
#           --------------
#                  9
#           If, Elif, & Else
#           Slicing (strings)
#           Boolean Operators
#  Dictionaries (found in today's bonus)
#
#                  10
#         Try-Except, Continue
#              Exceptions
# ***************************************
# ***************************************

"""
while True:
    user_action = input("Type add, show, edit, complete, or exit:  ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        with open("todos.txt",'r') as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

        message = f"\n'{user_action[4:]}' has been added to the list!\n"
        print(message)

    elif user_action.startswith("show"):
        file = open("todos.txt", 'r')
        todos = file.readlines()
        file.close()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            with open("todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter a new task: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

            message = f"\n'{completed_todo}' was removed from the list!\n"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("\n" + "Bye!")
"""

# ***************************************
# ***************************************
#               Day 11
#           --------------
#       Avoiding Repetitive Code
#         w/ Custom Functions
# ***************************************
# ***************************************

"""
def get_todos():
    with open("todos.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add, show, edit, complete, or exit:  ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        with open("todos.txt", 'w') as file:
            file.writelines(todos)

        message = f"\n'{user_action[4:]}' has been added to the list!\n"
        print(message)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new task: ")
            todos[number] = new_todo + "\n"

            with open("todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            with open("todos.txt", 'w') as file:
                file.writelines(todos)

            message = f"\n'{completed_todo}' was removed from the list!\n"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("\n" + "Bye!")
"""

# **************************************
# **************************************
#               Day 12
#           --------------
#         Custom Functions w/
#              Arguments
#          Multiple Arguments
# **************************************
# **************************************

"""
def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete, or exit:  ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos("todos.txt")

        todos.append(todo + "\n")

        write_todos("todos.txt", todos)

        message = f"\n'{user_action[4:]}' has been added to the list!\n"
        print(message)

    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter a new task: ")
            todos[number] = new_todo + "\n"

            write_todos("todos.txt", todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")
            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos.txt", todos)

            message = f"\n'{completed_todo}' was removed from the list!\n"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("Bye!")
"""


# **************************************
# **************************************
#            Day 13, onward.
# **************************************
# **************************************

from functions import get_todos, write_todos
import time


now = time.strftime("%b %d, %Y, %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete, or exit:  ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

        message = f"\n'{user_action[4:]}' has been added to the list!\n"
        print(message)

    elif user_action.startswith("show"):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter a new task: ")
            todos[number] = new_todo + "\n"

            write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            completed_todo = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"\n'{completed_todo}' was removed from the list!\n"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print("\n" + "Bye!")
