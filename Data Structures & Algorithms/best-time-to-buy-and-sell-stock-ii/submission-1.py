class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        memo ={}
        def dfs(i, stock):
            if i >= len(prices):
                return 0

            if (i, stock) in memo:
                return memo[(i, stock)]

            # sell, buy, keep
            res = dfs(i+1, stock) + 0


            p = prices[i]
            if stock==0:
                res = max(res, dfs(i+1, 1) - p)
                
            else:
                res =max(res, dfs(i+1, 0) + p)

            
            
            memo[(i,stock)] = res

            return res

        return dfs(0, 0)