# Fibonacci series is defined as f(n) = f(n-1) + f(n-2) with f(0) = 0
#             and f(1) = 1. Hence the series is 0, 1, 1, 2, 3, 5, 8,... Now:
# 	    a. Find the sum of first n Fibonacci numbers

def sum_fibonacci(n):
    sum = 0
    for i in range(n):
        sum += fibo(i)
    return sum

def fibo(n): # Define a function fibo which takes a number n as input
    first = 0 # Initialise the first fibonacci number as 0
    second = 1 # Initialise the second fibonacci number as 1

    third = first + second # Calculate the third fibonacci number as sum of first and second

    # Run a loop to calculate the remaining fibonacci numbers
    for i in range(0,n-3):
        first = second # Assign the second fibonacci number to the first
        second = third # Assign the third fibonacci number to the second
        third = first + second # Sum of first and second is third

    return third # Return the nth fibonacci number
    
n = input("Enter a number: ")
n = int(n)

print(f"The sum of first {n} Fibonacci numbers is {sum_fibonacci(n)}.")