# Given a string, print all possible permutations of the string. You can use python in-built features.
# Input : abc
# Output : abc acb bac bca cab cba

def permute_string(string):
    if len(string) == 1:
        return [string]
    else:
        perms = []
        for i in range(len(string)):
            for perm in permute_string(string[:i] + string[i+1:]):
                perms.append(string[i] + perm)
        return perms
    
string = input("Enter a string: ")
print(permute_string(string))