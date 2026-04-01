class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        # store n x n matrix
        memo = [[-1] * (n) for _ in range(n)] # i,j
        # memo = [-1] * n

        def dfs(i, j):

            if i >= len(nums):
                return 0

            if j != -1 and memo[i][j] != -1:
                return memo[i][j]

            # at each step take or not 2 ** n

            a = dfs(i+1, j) # skip

            b = 0
            if j == -1 or nums[i] > nums[j]:
                b = dfs(i+1, i) + 1 # include

            memo[i][j] = max(a, b)
            return max(a, b)

        return dfs(0, -1)