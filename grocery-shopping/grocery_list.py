
grocery_list = []


def add(item):
    grocery_list.append(item)


def add(*items):
    for i in items:
        grocery_list.append(i)


def exclude(item):
    grocery_list.remove(item)


def get_list():
    return grocery_list


def alter(item, new_item):
    grocery_list[grocery_list.index(item)] = new_item
