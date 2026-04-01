class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        occur = defaultdict(int)

        for i,n in enumerate(nums):
            if n not in occur:
                occur[n] = i
            elif n in occur:
                j = occur[n]
                if abs(i-j) <= k:
                    return True
                occur[n] = i
        return False