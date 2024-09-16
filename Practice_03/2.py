def find_missing_number(lst):
    # First find the maximum number in the list
    n = max(lst)
    # Create a set of the list elements
    lst_set = set(lst)
    # Create a set of all numbers from 1 to n
    n_set = set()
    for i in range(1, n + 1):
        n_set = n_set.union({i})
    # Find the difference between the two sets
    missing_number = n_set - lst_set
    return missing_number.pop()

lst = [1, 2, 3, 4, 5, 6, 7, 8, 10]
print(find_missing_number(lst))