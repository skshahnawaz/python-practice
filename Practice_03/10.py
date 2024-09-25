# If two consecutive odd numbers are prime, then they are called as twin primes. Write a function to print twin primes less 
# than n.

# Input : 1000
# Output :
# 3 and 5 
# 5 and 7 
# ... 
# 881 and 883

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def twin_primes(n):
    for i in range(3, n):
        if is_prime(i) and is_prime(i+2):
            print(i, "and", i+2)

n = int(input("Enter a number: "))
twin_primes(n)