import random

"""def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = int(arr[i])
        j = i - 1
        while j >= 0 and isinstance(arr[j], dict) and int(arr[j]) > x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > x:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
