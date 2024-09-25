# Given a dictionary with different values. Print all the keys of the dictionary where the value is less than 5.
# Input: { 'A' : 5, 'H' : 7, 'K' : 2, 'I' : 0 }
# Output:
# K
# I

def print_keys(dictionary):
    for key in dictionary.keys():
        if dictionary[key] < 5:
            print(key)

dictionary = { 'A' : 5, 'H' : 7, 'K' : 2, 'I' : 0 }
print_keys(dictionary)