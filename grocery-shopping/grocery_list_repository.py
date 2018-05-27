import pickle
import grocery_list

file_name = "grocery-list.data"


def persist(items):
    with open(file_name, "wb") as f:
        pickle.dump(items, f)


def read():
    items = []
    with open(file_name, "rb") as f:
        items = pickle.load(f)
    return items


def update(item, new_item):
    items = read()
    items[items.index(item)] = new_item
    with open(file_name, "r+b") as f:
        pickle.dump(items, f)


def delete(item):
    items = read()
    items.remove(item)
    with open(file_name, "r+b") as f:
        items = grocery_list.get_list()
        pickle.dump(items, f)
