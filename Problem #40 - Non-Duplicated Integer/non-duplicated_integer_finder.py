def find_unique(arr):
    result_arr = [0] * 32
    for num in arr:
        for i in range(32):
            bit = num >> i & 1
            result_arr[i] = (result_arr[i] + bit) % 3

    result = 0
    for i, bit in enumerate(result_arr):
        if bit:
            result += 2 ** i

    return result