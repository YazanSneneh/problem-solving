
def find_larges_smallest_number_built_in_method(numbers):
    length = len(numbers)
    if len(numbers) < 1:
        return
    numbers.sort()
    return numbers[0], numbers[length-1]

def find_larges_smallest_number(numbers):
    length = len(numbers)

    if length <1:
        return

    smallest = largest = numbers[0]

    for i in range(length -1):
        if smallest > numbers[i]:
            smallest = numbers[i]

        if largest < numbers[i]:
            largest = numbers[i]

    return smallest, largest