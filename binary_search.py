import random


def binary_search(list_search=[], key=0, start=0, end=0):
    print(f'searching {key} between {start} and {end - 1}')
    if start > end:
        return False
    middle = (start + end) // 2

    if list_search[middle] == key:
        return True
    elif list_search[middle] < objective_key:
        return binary_search(list_search, key, middle + 1, end)
    else:
        return binary_search(list_search, key, start, middle - 1)


if __name__ == '__main__':
    list_size = int(input('What size the list have?:'))
    objective_key = int(input('Which number do you want to search in the previous list?'))

    list_to_search = [random.randint(0, 100) for x in range(list_size)]
    found = binary_search(list_to_search, objective_key, 0, len(list_to_search))
    print(list_to_search)
    print(f'The elemet {objective_key} {"is" if found else "is not"} on the list')
