def power(x, y):
    if y < 0:
        return power(1 / x, -y)
    elif y == 0:
        return 1
    elif y == 1:
        return x
    elif y % 2 == 0:
        return power(x * x, y // 2)
    else: # y is odd
        return x * power(x * x, y // 2)