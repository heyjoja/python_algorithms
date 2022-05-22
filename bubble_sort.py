import random


def bubble_sort(list_to_work) -> list:
    n = len(list_to_work)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list_to_work[j] > list_to_work[j + 1]:
                list_to_work[j], list_to_work[j + 1] = list_to_work[j + 1], list_to_work[j]
    return list(set(list_to_work))


if __name__ == '__main__':
    list_size = int(input('What list size do you want?'))
    list_to_order = [random.randint(0, 100) for i in range(list_size)]
    print(f'List to order {list_to_order} \n')
    list_ordered = bubble_sort(list_to_order)
    print(f'List ordered {list_ordered}')
