class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ret = []

        p = 1
        zeros=0
        for n in nums:
            if n != 0:
                p *= n
            else:
                zeros+=1
        for n in nums:
            if n == 0:
                if zeros == 1:
                    ret.append(p)
                else:
                    ret.append(0) # there outer prod is 0
            else:
                if zeros:                
                    ret.append(0)
                else:
                    ret.append(p // n)
        
        return ret