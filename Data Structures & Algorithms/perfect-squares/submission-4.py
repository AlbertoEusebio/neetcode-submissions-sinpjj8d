from math import sqrt
class Solution:
    def numSquares(self, n: int) -> int:

        dp = [n] * (n+1)
        dp[0] = 0
        
        # n is the max: 1**2 + 1**2 + ... = n
        # 0 n n n n
        # 0 1 n n n
        for target in range(1, n+1):
            for s in range(1, target+1):
                if target - s**2 < 0:
                    break
                dp[target] = min(dp[target], 1+dp[target-s**2])

        return dp[n] 