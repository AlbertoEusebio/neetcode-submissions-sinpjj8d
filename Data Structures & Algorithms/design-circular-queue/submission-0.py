class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.l = [-1]*k
        self.ln = 0
        self.i = 0
        self.e = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        self.l[self.e] = value
        self.e += 1
        self.ln += 1
        if self.e == self.k:
            self.e %= self.k # go to 0
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.i += 1
        self.ln -= 1
        if self.i == self.k:
            self.i %= self.k

        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.l[self.i]

    def Rear(self) -> int:        
        if self.isEmpty():
            return -1
        return self.l[(self.e-1)%self.k]

    def isEmpty(self) -> bool:
        return self.ln == 0

    def isFull(self) -> bool:
        return self.ln == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()