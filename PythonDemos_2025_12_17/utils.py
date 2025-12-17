import os
import json

todos = []
FILE_NAME = "todos.json"

def load_todos():
    global todos
    if os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "r")
        todos = json.load(file)


def save_todos():
    global todos
    file = open(FILE_NAME, "w")
    json.dump(todos, file)


def print_todos():
    for i, todo in enumerate(todos, start=1):
        print(f"{i}. {todo}")

def print_menu():
    print("\nToDo Menu")
    print("1. View ToDos")
    print("2. Add a ToDo")
    print("3. Remove a ToDo")
    print("4. Exit")


def remove_todo():
    if len(todos) == 0:
        print("No ToDos!")
    else:
        print_todos()
        num_as_string = input("Enter a number to remove: ")
        if not num_as_string.isdigit():
            print("Invalid number!")
            return
        num = int(num_as_string)
        if num > len(todos) or num <= 0:
            print("Invalid number!")
        else:
            removed_todo = todos.pop(num - 1)
            print(f"Removed {removed_todo} from the list")

def print_message(message):
    print(message)

def add_todo():
    todo = input("Enter a new todo: ")
    if todo.strip() == "":
        print("Entry cannot be empty!")
    else:
        todos.append(todo.strip())
        print_message("Todo added!")


def list_todos():
    if len(todos) == 0:
        print("No ToDos!")
    else:
        print_todos()
