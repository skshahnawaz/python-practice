# 0 1 1 2 3 5 8 11

# Every number is sum of previous two numbers

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


n = int(input("Enter value of n : ")) # Take the value of n from user as input

print(fibo(n)) # Call the function fibo and pass the value n into it