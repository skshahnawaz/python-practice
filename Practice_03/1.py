# Write a function to rotate a list of integers in the range [1, n] by k steps to the right.

def rotate_list(lst, k):
    # Handle the case when k is greater than the length of the list
    if k>len(lst):
        k = int(k%len(lst))
    # Perform the rotation
    lst = (lst[-k:] + lst[:-k])
    return lst

n = int(input("Enter the number of elements in the list: "))
lst = [] # Create an empty list
# Add elements to the list
for i in range(1,n+1):
    lst.append(i)

# Get the rotation count from the user
k = int(input("Enter the number of steps to rotate: "))
print(rotate_list(lst, k))