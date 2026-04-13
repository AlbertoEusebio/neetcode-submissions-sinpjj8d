from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:

        if n == 0:
            return 0

        dp = {}

        def dfs(target):

            if target == 0:
                return 0

            if target in dp:
                return dp[target]

            res = target
            for i in range(target, 0, -1):
                if i**2 > target:
                    continue
                res = min(res, 1 + dfs(target - i**2))

            dp[target] = res
            return res
        
        return dfs(n)