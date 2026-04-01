class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}

        for i, n in enumerate(nums):
            if n in remaining:
                return [remaining[n], i]
            if target - n in remaining:
                continue
            remaining[target - n] = i
