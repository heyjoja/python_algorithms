def backpack(backpack_size, weights, values, n):
    if n == 0 or backpack_size == 0:
        return 0

    if weights[ n - 1 ] > backpack_size:
        return backpack(backpack_size, weights, values, n - 1)

    return max(values[n - 1] + backpack(backpack_size - weights[n - 1], weights, values, n - 1),
               backpack(backpack_size, weights, values, n - 1))


if __name__ == '__main__':
    values = [60, 100, 120]
    weights = [10, 20, 30]
    backpack_size = 50
    n = len(values)
    result = backpack(backpack_size, weights, values, n)
    print(result)