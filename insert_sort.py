import random


def insertion_sort(list_to_sort):
    for index in range(1, len(list_to_sort)):
        current_value = list_to_sort[index]
        current_position = index
        while current_position > 0 and list_to_sort[current_position - 1] > current_value:
            list_to_sort[current_position] = list_to_sort[current_position - 1]
            current_position -= 1
        list_to_sort[current_position] = current_value
    return list_to_sort


if __name__ == '__main__':
    list_a = [random.randint(0, 100) for x in range(10)]
    print(list_a)
    print(insertion_sort(list_a))
