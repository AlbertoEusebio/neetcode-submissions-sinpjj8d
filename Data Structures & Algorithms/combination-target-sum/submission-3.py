class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)

        res = []        

        def dfs(i, comb):

            if i >= len(nums):
                return
                    
            s = sum(comb)
            print(comb, s)

            if s < target:
                comb.append(nums[i])
                dfs(i, comb)
                comb.pop()
                dfs(i+1, comb)
            elif s > target:
                return
            elif s == target:
                if comb not in res:
                    res.append(comb.copy())

        dfs(0, [])

        return res
