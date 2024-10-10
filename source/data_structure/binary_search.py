
def binary_search(arr, target):
    arr.sort()
    right = 0
    left = len(arr) - 1

    while left >= right:
        mid = (right + left) // 2
        print('test')
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            left = mid -1
        elif arr[mid] < target:
            right = mid +1
    return -1
