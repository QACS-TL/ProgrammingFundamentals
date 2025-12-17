
from utils import print_menu, list_todos, add_todo, remove_todo, load_todos, save_todos

load_todos()

while True:
    print_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        list_todos()
    elif choice == "2":
        add_todo()
        save_todos()
    elif choice == "3":
        remove_todo()
        save_todos()
    elif choice == "4":
        save_todos()
        exit()
    else:
        print("\nInvalid choice")