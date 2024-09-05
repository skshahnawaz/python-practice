# Find sum of prime numbers between 1000 and 2000.

def is_prime(n):
    is_prime = True
    if (n < 2):
        is_prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
    return is_prime

sum = 0

for i in range(1000, 2001):
    if is_prime(i):
        sum += i

print(f"Sum of prime numbers between 1000 and 2000 is {sum}.")