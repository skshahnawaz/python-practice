# Check if a number n is prime. Convert the above solution to a function.

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

n = input("Enter a number: ")
n = int(n)

if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")