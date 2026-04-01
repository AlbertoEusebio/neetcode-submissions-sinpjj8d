class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        MIN_INT = -1001 * len(nums)

        def dfs(i, s):

            if i >= len(nums):
                return s

            if s != MIN_INT:
                b = dfs(i+1, s+nums[i])
            else:
                b = dfs(i+1, nums[i])
            
            # skip or take
            a = dfs(i+1, MIN_INT) # skip
            
            res = max(a, b, s)
            
            return res

        return dfs(0, MIN_INT)
