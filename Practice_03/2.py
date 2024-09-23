# Write a function that takes an unsorted list of integers from 1 to n, where one number is missing, and returns the missing
# number. Note that the value of n is the maximum number found in the input sequence, and is not provided separately.

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

#take the input from the user iteratively
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    lst.append(int(input("Enter the element: ")))
print(find_missing_number(lst))