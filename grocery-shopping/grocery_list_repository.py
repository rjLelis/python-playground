import pickle
from pathlib import Path

file = Path("grocery-list.data")


def persist(items):
    with open(file, "wb") as f:
        pickle.dump(items, f)


def read():
    items = []
    if file.is_file():
        with open(file, "rb") as f:
            items = pickle.load(f)
    return items


def delete(item):
    items = read()
    items.remove(item)
    with open(file, "r+b") as f:
        pickle.dump(items, f)
