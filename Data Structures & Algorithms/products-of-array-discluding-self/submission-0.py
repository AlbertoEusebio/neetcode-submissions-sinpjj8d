class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod(num):
            p = 1
            for n in num:
                p *= n
            return p
        p = []
        for i in range(len(nums)):
            p.append(prod(nums[:i] + nums[i+1:]))

        return p