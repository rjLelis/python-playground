import grocery_list_repository

items = grocery_list_repository.read()


def options(option):
    if option == 1:
        item = input("Enter the item: ")
        global items
        items.append(item)
        grocery_list_repository.persist(items)
        print(f"Item {item} saved in the list")
        return 0
    elif option == 2:
        item = input("Enter the item you want to remove: ")
        items.remove(item)
        grocery_list_repository.persist(items)
        print(f"Item {item} removed from the list")
        return 0
    elif option == 3:
        print("Items - ")
        if grocery_list_repository.read():
            items = grocery_list_repository.read()
            for item in items:
                print(item, end=" ")
            print()
        else:
            print("Empty list")
        return 0
    elif option == 0:
        return 1


def main():
    option = 0
    while True:
        print("1 - Add item to the list")
        print("2 - Delete item from the list")
        print("3 - Get all items from the list")
        print("0 - Exit")
        option = options(int(input("> ")))
        if option == 1:
            break


if __name__ == '__main__':
    main()
