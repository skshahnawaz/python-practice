import math

# function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# function to find the prime pair with the smallest primes that sum to N
def goldbach_variant_simpler(n):
    for p in range(2, n):
        if is_prime(p) and is_prime(n - p):
            return (p, n - p)

# Example run
n1 = 18

print("Prime pair for", n1, "is:", goldbach_variant_simpler(n1))
