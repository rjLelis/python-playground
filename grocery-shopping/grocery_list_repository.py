import pickle
from pathlib import Path

file = Path("grocery-list.data")


def persist(items):
    '''stores a list in a file'''
    with open(file, "wb") as f:
        pickle.dump(items, f)


def read():
    '''get all items and returns a list'''
    items = []
    if file.is_file():
        with open(file, "rb") as f:
            items = pickle.load(f)
    return items


def delete(item):
    '''deletes a item from the list and updates de file'''
    items = read()
    items.remove(item)
    with open(file, "r+b") as f:
        pickle.dump(items, f)
