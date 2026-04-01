class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i,j = 0, len(nums)
        m = (i+j)//2
        while i < j:
            if nums[m] == target:
                return m
            elif nums[m] > target:
                j = m-1
                if m-1 < 0 or nums[m-1] < target:
                    return m
            elif nums[m] < target:
                i = m+1
                if m+1 >= len(nums) or nums[m+1] > target:
                    return m+1
            m = (i+j)//2
        return m