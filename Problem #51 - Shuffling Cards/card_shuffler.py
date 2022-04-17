import random

def shuffle(arr):
    n = len(arr)
    for i in range(n - 1):
        j = random.randint(i, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr