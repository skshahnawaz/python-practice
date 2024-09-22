# List, Set, tuple, dict - to store collection of values in a single variable

# int. bool. string. float - to store single values in a single variable

# to store single value
# i = 10 # integer
# j = 9.5 #Float
# str = "Hello" #string
# val = True/False #boolean

#List

list1 = ["apple", "apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True]

# to access a single item
print(list1[2])
print(list1[-1])

# to access multiple items
print(list1[0:2])

#how to check if an item exists in a list
if (10 in list2):
    print("10 exists in list2")

list2[1] = "guava"

