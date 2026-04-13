class Solution:
    def integerBreak(self, n: int) -> int:
        
        memo = {}

        def dfs(m):
            

            if m == 1:
                return 1
            if m in memo:
                return memo[m]

            res = m if m != n else 0 # decompose in all 1 x 1
            for i in range(1, m):
                res = max(res, dfs(i) * dfs(m-i))
            
            memo[m] = res
            return res
        
        return dfs(n)