class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums = sorted(nums)

        def dfs(i, sub):

            if i >= len(nums):
                return

            sub.append(nums[i])
            res.append(sub.copy())

            print(sub, i)

            dfs(i+1, sub.copy())
            sub.pop()
            j = i+1
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            dfs(j, sub.copy())

        dfs(0, [])

        return res