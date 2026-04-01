class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        stk = self.stocks.copy()
        res = 1
        while stk:
            n = stk.pop()
            if n > price:
                break
            res += 1
        self.stocks.append(price)
        return res

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)