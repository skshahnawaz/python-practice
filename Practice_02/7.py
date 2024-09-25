# Given a list consisting integers 0, 1, and 2, sort it without using any in-built functions. 
# Input : 0 2 1 2 0 1 0
# Output : 0 0 0 1 1 2 2

# Take the list as input from user

def sort_list(list):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in list:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        elif i == 2:
            count_2 += 1
    for i in range(0, count_0):
        list[i] = 0
    for i in range(count_0, count_0 + count_1):
        list[i] = 1
    for i in range(count_0 + count_1, count_0 + count_1 + count_2):
        list[i] = 2
    return list

n = int(input("Enter number of elements in the list: "))
list = []
for i in range(0,n):
    list.append(int(input("Enter an element: ")))

print(sort_list(list))