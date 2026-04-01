class Solution:
    def climbStairs(self, n: int) -> int:
        # Search binary tree
        sums = {}

        def dfs(s):
            if s > n:
                return 0
            if s == n:
                return 1
            print(s)
            if s+1 not in sums:
                sums[s+1] = dfs(s+1)
            if s+2 not in sums:
                sums[s+2] = dfs(s+2)
            return sums[s+1] + sums[s+2]
        
        return dfs(0)