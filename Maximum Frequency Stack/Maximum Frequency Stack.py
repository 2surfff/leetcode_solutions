from collections import deque

class FreqStack:
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0

    def push(self, x: int) -> None:
        if x in self.freq:
            self.freq[x] += 1
        else:
            self.freq[x] = 1
        i = self.freq[x]

        if i >= self.max_freq:
            self.max_freq = i
        if i not in self.group:
            self.group[i] = deque()
        self.group[i].append(x)

    def pop(self) -> int:
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            self.max_freq -= 1
        return val
