# Search unordered lists


def search_unordered_1(alist, item):
    found = False
    for value in alist:
        if value == item:
            found = True
    return found


def search_unordered_2(alist, item):
    found = False
    position = 0
    while not found and position < len(alist):
        if alist[position] == item:
            found = True
        else:
            position = position + 1

    return found, position

# Search ordered lists


def search_ordered(alist, item):
    found = False
    stop = False
    position = 0
    while not found and not stop:
        if alist[position] == item:
            found = True
        elif alist[position] > item or position > len(alist)-1:
            stop = True
        else:
            position = position + 1
    return found, position






