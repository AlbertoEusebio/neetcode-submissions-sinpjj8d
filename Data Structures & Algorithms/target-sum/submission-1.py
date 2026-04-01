class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        n = len(nums)

        memo = {}

        def dfs(i, s):

            if i >= n and s != target:
                return 0
            elif i >= n and s == target:
                return 1
            
            if (i, s) in memo:
                return memo[(i, s)]

            print(nums[i], s)

            a = dfs(i+1, s - nums[i]) + dfs(i+1, s + nums[i])

            memo[(i, s)] = a

            return a

        return dfs(0, 0)