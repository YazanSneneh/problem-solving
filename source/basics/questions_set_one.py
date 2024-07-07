
def add(number_one=0, number_two=0):
    return number_one + number_two

def factorial(number):
    result = 1
    for i in range(1, abs(number)+1):
        result *= i
    return result

def fibonacci_sequence(number):
    fibonacci_sequence = [1, 1]

    if number < 1:
        return []

    if number == 1:
        return [1]

    if number == 2:
        return fibonacci_sequence

    [fibonacci_sequence.append(fibonacci_sequence[i-1] + fibonacci_sequence[i]) for i in range(1, number+1)]

    return fibonacci_sequence


def reverse_string(str):
    return str[::-1]