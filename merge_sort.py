import random


def merge_sort(list_to_order):
    if len(list_to_order) > 1:
        middle = len(list_to_order) // 2
        right = list_to_order[:middle]
        left = list_to_order[middle:]

        # recursive call in each middle
        merge_sort(right)
        merge_sort(left)
        # iterators to traverse the two sub lists
        i = 0
        j = 0
        # iterators to traverse the principal list
        k = 0

        while i < len(right) and j < len(left):
            if right[i] < left[j]:
                list_to_order[k] = right[i]
                i += 1
            else:
                list_to_order[k] = left[j]
                j += 1
            k += 1

        while i < len(right):
            list_to_order[k] = right[i]
            i += 1
            k += 1

        while j < len(left):
            list_to_order[k] = left[j]
            j += 1
            k += 1
        print(f'izquierda {right} {"-" * 5} derecha {left}')
        return list_to_order


if __name__ == '__main__':
    list_size = int(input('What size the list have?:'))
    list_to = [random.randint(0, 100) for x in range(list_size)]
    print(list_to)
    print('-' * 20)
    list_ordered = merge_sort(list_to)
    print(list_ordered)
