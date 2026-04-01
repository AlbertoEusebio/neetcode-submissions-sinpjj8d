class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(i, path):

            if i >= len(nums):
                return len(path)

            # at each step take or not

            a = dfs(i+1, path) # skip

            b = 0
            if path == [] or nums[i] > path[-1]:
                path.append(nums[i])
                b = dfs(i+1, path)
                path.pop()

            return max(a, b)

        return dfs(0, [])