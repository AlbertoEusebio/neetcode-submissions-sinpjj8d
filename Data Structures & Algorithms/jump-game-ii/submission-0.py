class Solution:
    def jump(self, nums: List[int]) -> int:
        

        MAX_JUMPS = len(nums) + 10

        def dfs(i, s):

            if i >= len(nums) -1:
                return s

            power = nums[i]

            m = MAX_JUMPS
            for p in range(power, 0, -1):
                a = dfs(i+p, s+1)
                if a < m:
                    m = a
            
            return m

        return dfs(0, 0)