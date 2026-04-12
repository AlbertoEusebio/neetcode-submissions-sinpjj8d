class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        if target == 0:
            return 1 # [] empty is comb

        nums = sorted(nums)

        dp = {}

        def dfs(i, s):

            if (i, s) in dp:
                return dp[(i, s)]

            if s == target:
                return 1
            elif i == len(nums) or s > target:
                return 0

            # print(i, nums[i], s)
            res = 0
            for j,n in enumerate(nums):
                res += dfs(j, s+n)
            
            dp[(i, s)] = res
            return res

        res = 0
        for i,n in enumerate(nums):
            res += dfs(i, n)

        return res