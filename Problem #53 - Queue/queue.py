class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, val):
        self.s1.append(val)

    def dequeue(self):
        if self.s2:
            return self.s2.pop()
        if self.s1:
            # empty all of s1 into s2
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        return None