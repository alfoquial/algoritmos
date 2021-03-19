# binary search ordered lists
# not recursive


def binary_search(a_list, item):
    found = False
    first = 0
    last = len(a_list) - 1
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            found = True
        else:
            if a_list[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


# Recursive


def binary_research(a_list, item):
    found = False
    first = 0
    last = len(a_list) - 1
    if first <= last and not found:
        midpoint = (first+last)//2
        if a_list[midpoint] == item:
            found = True
        elif a_list[midpoint] <= item:
            return binary_research(a_list[midpoint + 1:], item)
        else:
            return binary_research(a_list[:midpoint], item)
    return found
