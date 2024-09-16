def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b
    
n = int(input("Enter the value of n: "))
print(f'The {n}th Fibonacci number is {fibonacci(n)}')