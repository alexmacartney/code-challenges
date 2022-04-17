def longest_palindrome(s):
    if not s:
        return ''

    longest = s[0]
    A = [[None for _ in range(len(s))] for _ in range(len(s))]

    # Set all substrings of length 1 to be true
    for i in range(len(s)):
        A[i][i] = True

    # Try all substrings of length 2
    for i in range(len(s) - 1):
        A[i][i + 1] = s[i] == s[i + 1]

    i, k = 0, 3
    while k <= len(s):
        while i < (len(s) - k + 1) :
            j = i + k - 1
            A[i][j] = A[i + 1][j - 1] and s[i] == s[j]
            # Update longest if necessary
            if A[i][j] and len(s[i:j + 1]) > len(longest):
                longest = s[i:j + 1]
            i += 1
        k += 1
        i = 0
    return longest