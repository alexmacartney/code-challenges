def count_inversions(arr):
    count, _ = count_inversions_helper(arr)
    return count

def count_inversions_helper(arr):
    if len(arr) <= 1:
        return 0, arr
    mid = len(arr) // 2
    a = arr[:mid]
    b = arr[mid:]
    left_count, left_sorted_arr = count_inversions_helper(a)
    right_count, right_sorted_arr = count_inversions_helper(b)
    between_count, sorted_arr = merge_and_count(left_sorted_arr, right_sorted_arr)
    return left_count + right_count + between_count, sorted_arr

def merge_and_count(a, b):
    count = 0
    sorted_arr = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            sorted_arr.append(a[i])
            i += 1
        elif a[i] > b[j]:
            sorted_arr.append(b[j])
            count += len(a) - i
            j += 1
    sorted_arr.extend(a[i:])
    sorted_arr.extend(b[j:])
    return count, sorted_arr