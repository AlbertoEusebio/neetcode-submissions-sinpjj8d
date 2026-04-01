class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        # stk = self.stocks.copy()
        span = 1
        while self.stocks and self.stocks[-1][0] <= price:
            n = self.stocks.pop()
            span += n[1]
        self.stocks.append((price, span))
        return span
        # if self.stocks == []:
        #     self.stocks.append(price)
        #     self.spans.append(1)
        #     return 1

        # n = self.stocks[-1]
        # if n <= price:
        #     self.stocks.append(price)
        #     self.spans.append(self.spans[-1]+1)
        #     return self.spans[-1]
        
        # self.stocks.append(price)
        # self.spans.append(1)
        # return self.spans[-1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)