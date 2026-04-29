class FreqStack:

    def __init__(self):
        self.heap = []
        self.freq ={}
        self.l =0

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0)+1
        self.freq[val] = f
        self.l +=1
        heapq.heappush(self.heap, (-f, -self.l, val))

    def pop(self) -> int:
        f, l, v = heapq.heappop(self.heap)
        self.freq[v] -=1
        # print(self.heap)
        #if -f -1 > 0:
          #  heapq.heappush(self.heap, (f+1, v))
        return v


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()