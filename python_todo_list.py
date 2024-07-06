# ask user what task they wish to do
# if add, collect items and add to todo_list
# if remove, ask items to remove and remove them
# if view, display items in todo_list
# if quit, quit


def main():

    todo_list = []
    while True:
        task = input(
            "Type a task('A' to Add, 'R' to remove, 'V' to view, 'Q' to quit):\n").upper()
        if task == "A":
            todo_list = add_items(todo_list)
        elif task == "R":
            todo_list = remove_items(todo_list)
        elif task == "V":
            view_items(todo_list)
        elif task == "Q":
            print("GoodBye!!!")
            break
        else:
            print("Invalid Input")


def add_items(todo_list):
    while True:
        item = input("Enter item to Add, 'Q' to go back: ").title()
        if item == "Q":
            break
        elif item in todo_list:
            print(f"{item} already in list")
        else:
            todo_list.append(item)
            print()
            print("------------------------")
            print(f"{item} has been Added")
            print("------------------------")
            print()

    return todo_list


def remove_items(todo_list):
    while True:
        if todo_list:
            item = input("Enter item to remove, 'Q' to go back: "). title()
            if item in todo_list:
                todo_list.remove(item)
                print()
                print("------------------------")
                print(f"{item} has been Removed")
                print("------------------------")
                print()

            elif item == "Q":
                break
            else:
                print(f"{item} not in Todo List")
        else:
            print("Todo list is empty")
            break
    return todo_list


def view_items(todo_list):
    if todo_list:
        print()
        print("---------------------------------------")
        print(f"List Contains {len(todo_list)} Items:")
        print("---------------------------------------")
        for index, char in enumerate(todo_list):
            print(f"{index + 1}. {char}")
        print("---------------------------------------")
        print()
    else:
        print("List is empty!")


if __name__ == "__main__":
    main()
