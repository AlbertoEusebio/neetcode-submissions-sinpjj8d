class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0, len(nums)-1

        while i < j:
           # n,m = nums[i], nums[j]

            while j>=0 and nums[j] == val:
                nums.pop()
                j-=1
            
            if i< len(nums) and nums[i] == val:
                t = nums[j]
                nums[j] = nums[i]
                nums[i] = t
            i+=1
        
        while j>=0 and nums[j] == val:
                nums.pop()
                j-=1
        return len(nums)
            