import grocery_list
import grocery_list_repository


def main():
    option = 0
    while True:
        print("1 - Add item to the list")
        print("2 - Update item from the list")
        print("3 - Delete item from the list")
        print("4 - Get all items from the list")
        print("5 - Save list")
        print("0 - Exit")
        option = int(input("> "))

        if option == 1:
            item = input("Enter the item: ")
            grocery_list.add(item.title())
        elif option == 2:
            item = input("Enter the item you want to replace: ")
            new_item = input("Enter the new item to store on the list: ")
            grocery_list.alter(item, new_item)
        elif option == 3:
            item = input("Enter the item you want to remove: ")
            grocery_list.exclude(item)
        elif option == 4:
            print("Items - ")
            print(grocery_list_repository.read())
        elif option == 5:
            grocery_list_repository.persist(grocery_list.get_list())
        elif option == 0:
            break

if __name__ == '__main__':
    main()
