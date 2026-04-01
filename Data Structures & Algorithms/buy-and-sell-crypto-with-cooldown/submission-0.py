class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dfs(i, n, prof):

            if i >= len(prices):
                return prof

            print(prices[i])

            # can sell
            a = 0 
            if n == 1 and prices[i]+prof > 0:
                # if sell can't buy next day nor sell, so skip
                a=dfs(i+2, 0, prof + prices[i])
            # can buy
            elif n == 0:
                a=dfs(i+1, 1, prof - prices[i])
            
            # skip
            b = dfs(i+1, n, prof)

            return max(a,b)


        return dfs(0, 0, 0)
