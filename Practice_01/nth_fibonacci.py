# Fibonacci series is defined as f(n) = f(n-1) + f(n-2) with f(0) = 0
#             and f(1) = 1. Hence the series is 0, 1, 1, 2, 3, 5, 8,... Now:
# 	    a. Find the n'th value of the series

def nth_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)
    
n = input("Enter a number: ")
n = int(n)

print(f"The {n}th value of the Fibonacci series is {nth_fibonacci(n)}.")