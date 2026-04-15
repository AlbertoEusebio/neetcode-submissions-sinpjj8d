class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        memo = {}

        def dfs(i, s):

            if i == len(stones):
                return abs(s)

            if (i, s) in memo:
                return memo[(i, s)]

            # assign value to remaining
            a = dfs(i+1, s + stones[i])
            b = dfs(i+1, s - stones[i])

            memo[(i, s)] = min(a, b) 

            return min(a, b)

        return dfs(0, 0)