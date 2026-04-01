class MinStack:

    def __init__(self):
        self.stk = []
        self.minima = []

    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minima == [] or val < self.stk[self.minima[-1]]:
            self.minima.append(len(self.stk) - 1)

    def pop(self) -> None:
        i = len(self.stk) - 1
        if self.minima[-1] == i:
            self.minima = self.minima[:-1]
        self.stk = self.stk[:-1]
        
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.stk[self.minima[-1]]
