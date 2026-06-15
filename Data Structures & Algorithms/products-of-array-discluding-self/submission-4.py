class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # cum-prods
        forward = []
        backward = []

        p = 1
        for n in nums:
            p *= n
            forward.append(p)
        
        p = 1
        for n in nums[::-1]:
            p *= n
            backward.append(p)

        backward = backward[::-1]

        ret = []

        for i in range(len(nums)):
            b = backward[i+1] if i < (len(nums)-1) else 1
            f = forward[i-1] if i > 0 else 1
            p = b*f

            ret.append(p)

        return ret