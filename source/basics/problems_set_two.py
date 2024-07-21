def find_larges_smallest_number_built_in_method(numbers):
    length = len(numbers)
    if len(numbers) < 1:
        return
    numbers.sort()
    return numbers[0], numbers[length - 1]


def find_larges_smallest_number(numbers):
    length = len(numbers)
    if length < 1:
        return

    smallest = largest = numbers[0]

    for i in range(length):
        if smallest > numbers[i]:
            smallest = numbers[i]

        if largest < numbers[i]:
            largest = numbers[i]

    return smallest, largest


def missing_number(numbers):
    '''
    Q1
    Write a Python program that take n sequence from 0 to n can find number missing in sequence and return the missing number
    example: 0,1,2,4,5,6,7,8,9,10
    '''
    if len(numbers) == 0:
        return 0

    for i in range(max(numbers)+1):
        missing = i
        for j in range(i, max(numbers)+1):
            if missing not in numbers:
                return missing
    return max(numbers)+1


'''
Q2
Write a program tha return first appearance character not repeated
example: stress
output: t
'''

