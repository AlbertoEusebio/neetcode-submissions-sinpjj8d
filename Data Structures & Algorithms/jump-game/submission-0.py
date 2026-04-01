class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        def dfs(i):
            print(i)

            if i >= len(nums)-1:
                return True

            # if nums[i] == 0:
            #     return False

            power = nums[i]

            for p in range(power, 0, -1):
                if dfs(i+p):
                    return True
            
            return False
        
        return dfs(0)