class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_prod = None
        for l in range(len(nums), 0, -1):
            for i in range(len(nums)-l+1):
                p = 1
                print(nums[i:i+l])
                for n in nums[i:i+l]:
                    p *= n
                if max_prod is None or p > max_prod:
                    max_prod = p
        
        return max_prod