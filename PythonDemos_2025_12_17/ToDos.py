
from utils import print_menu, list_todos, add_todo, remove_todo

while True:
    print_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        list_todos()
    elif choice == "2":
        add_todo()
    elif choice == "3":
        remove_todo()
    elif choice == "4":
        exit()
    else:
        print("\nInvalid choice")