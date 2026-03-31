class MyQueue:

    def __init__(self):
        self.s1 = []

    def push(self, x: int) -> None:
        s2 = []
        for i in range(len(self.s1)):
            s2.append(self.s1.pop())
        s2.append(x)
        for i in range(len(s2)):
            self.s1.append(s2.pop())
        
        # self.s1 = s2
        print(self.s1)

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()