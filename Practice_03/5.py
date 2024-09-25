# Write a function that returns all elements that are present more than one time in a given list of integers. Use python functions only

def more_than_one(list):
    more_than_one = []
    for i in list:
        if list.count(i) > 1:
            more_than_one.append(i)
    return more_than_one

n = int(input("Enter number of elements in the list: "))
list = []
for i in range(0,n):
    list.append(int(input("Enter an element: ")))
