def rotate_list(lst, k):
    n = len(lst)
    k = k % n
    return lst[-k:] + lst[:-k]

n = int(input("Enter the number of elements in the list: "))
lst = list(range(1, n + 1))
k = int(input("Enter the number of steps to rotate: "))
print(rotate_list(lst, k))