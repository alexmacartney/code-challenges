def break_string(s, k):
    words = s.split()

    if not words:
        return []

    current = []
    all = []

    for i, word in enumerate(words):
        if length(current + [word]) <= k:
            current.append(word)
        elif length([word]) > k:
            return None
        else:
            all.append(current)
            current = [word]
    all.append(current)

    return all

def length(words):
    if not words:
        return 0
    return sum(len(word) for word in words) + (len(words) - 1)