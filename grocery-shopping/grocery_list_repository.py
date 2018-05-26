import pickle

file_name = "grocery-list.data"


def persist(items):
    with open(file_name, "wb") as f:
        pickle.dump(items, f)


def read():
    items = []
    with open(file_name, "rb") as f:
        items = pickle.load(f)
    return items


def update(items):
    with open(file_name, "r+b") as f:
        pickle.dump(items, f)
