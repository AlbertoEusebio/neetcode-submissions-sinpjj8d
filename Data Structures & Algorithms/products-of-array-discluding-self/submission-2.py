class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod(num):
            p = 1
            for n in num:
                p *= n
            return p

        pref = []

        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            pref.append(prod)
        
        suff = []
        prod = 1
        for n in nums[::-1]:
            prod *= n
            suff.append(prod)
        suff = suff[::-1]

        print(pref, suff)
        products = []
        for i in range(len(nums)):
            p = pref[i-1] if i-1 >= 0 else 1 
            s = suff[i+1] if i+1 < len(nums) else 1
            products.append(p * s)

        return products