class FreqStack:

    def __init__(self):
        self.freq = {}
        self.stacks = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        self.stacks[f].append(val)
        self.max_freq = max(self.max_freq, f)

    def pop(self) -> int:
        v = self.stacks[self.max_freq].pop()
        self.freq[v] -= 1
        if self.stacks[self.max_freq] == []:
            self.max_freq -= 1
        return v


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()