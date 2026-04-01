class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)

        res = []        

        def dfs(i, comb):

            if i >= len(nums):
                return
                    
            comb.append(nums[i])
            s = sum(comb)
            print(comb, s)

            if s < target:
                for k in range(i, len(nums)):
                    dfs(k, comb.copy())
            elif s > target:
                return
            elif s == target:
                if comb not in res:
                    res.append(comb.copy())

        for k in range(len(nums)):
            dfs(k, [])

        return res
