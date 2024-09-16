def is_key_present(dictionary, key):
    if key in dictionary:
        return "Yes"
    else:
        return "No"
    
dictionary = {'Name' : 'Ron', 'Age' : 22}
key = 'Name'
print(is_key_present(dictionary, key))
