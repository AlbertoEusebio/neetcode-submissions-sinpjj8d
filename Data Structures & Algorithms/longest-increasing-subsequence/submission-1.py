class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        # store n x n matrix
        # memo = [[-1] * (n) for _ in range(n)]
        memo = [-1] * n

        def dfs(i, j):

            if i >= len(nums):
                return 0

            # at each step take or not 2 ** n

            a = dfs(i+1, j) # skip

            b = 0
            if j == -1 or nums[i] > nums[j]:
                b = dfs(i+1, i) + 1 # include
 
            return max(a, b)

        return dfs(0, -1)