class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(nums)

        self.ret = []
        def dfs(i, s, curr):
            # print(i, s, curr)
            if i >= len(nums) or s > target:
                return
            if s == target:
                if curr not in self.ret:
                    self.ret.append(curr.copy())
                return

            # take and continue, take and stay or skip
            dfs(i, s+nums[i], curr + [nums[i]])
            dfs(i+1, s+nums[i], curr + [nums[i]])
            dfs(i+1, s, curr)

        dfs(0, 0, [])

        return self.ret