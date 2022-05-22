def lineal_search(list_validation, objective_key):
    """Lineal search, we need to validate if objective key exist
    into list_validation"""
    for x in range(len(list_validation)):
        if list_validation[x] != objective_key:
            continue
        return 'The objective key of %s is located in the position %s' % (objective_key, x)
    return 'The objective key of %s is not located' % (objective_key)


if __name__ == "__main__":
    list_validation = [1, 4, 3, 0, -1]
    objective_key = 44
    print(lineal_search(list_validation, objective_key))
