class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values = {}
        for i in nums:
            if i not in values:
                values[i] = 1
            else:
                return True
        return False