class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l, r = 0, len(nums)-1
        m = l + (r-l)//2

        while l <= r:
             
            if nums[m] == target:
                return True

            elif nums[l] < nums[m]:
                if target < nums[l] or target > nums[m]:
                    l = m+1
                else:
                    r = m-1 
            elif nums[l] > nums[m]:
                if target > nums[r] or target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                l+=1
            
            m = l + (r-l) // 2
        return False