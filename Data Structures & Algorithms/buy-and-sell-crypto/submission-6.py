class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1

        p = 0
        max_p = 0
        while j < len(prices):
            p = prices[j] - prices[i]
            print(i,j)
            if prices[j] < prices[i]:
                i = j
            
            if max_p < p:
                max_p = p

            j+=1

        return max_p