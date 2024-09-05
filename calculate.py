# Read n numbers. Find the following parameters:
#             a. Average
#             b. Maximum
#             c. Minimum
#             d. Second maximum
#             e. Second minimum

# Do not use any predefined functions. Implement your own logic.


def average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


def maximum(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max


def minimum(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min    


def second_maximum(numbers):
    max = maximum(numbers)
    second_max = numbers[0]
    for number in numbers:
        if number != max and number > second_max:
            second_max = number
    return second_max


def second_minimum(numbers):
    min = minimum(numbers)
    second_min = numbers[0]
    for number in numbers:
        if number != min and number < second_min:
            second_min = number
    return second_min