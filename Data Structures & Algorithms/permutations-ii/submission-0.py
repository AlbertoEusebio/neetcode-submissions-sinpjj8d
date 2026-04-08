class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        pick = [0] * len(nums)

        res = []
        def dfs(pk, pth):
            nonlocal res
            if len(pth) == len(nums):
                if pth not in res:
                    res.append(pth.copy())
                return

            for i in range(len(pk)):
                if pk[i] == 1:
                    continue
                pk[i] = 1
                dfs(pk, pth + [nums[i]])
                pk[i] = 0

        dfs(pick, [])
        return res