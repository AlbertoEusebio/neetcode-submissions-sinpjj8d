class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        # find pivot then bs
        l, r = 0, len(nums)-1

        m = (l+r+1) // 2
        while l <= r:
            if nums[m] == target:
                return True
            if nums[l] < nums[m]:
                # l --> m sorted
                if target < nums[l] or nums[m] < target:
                    l = m+1
                else:
                    r = m-1                
            elif nums[r] == nums[m]:
                r = r-1
            elif nums[l] == nums[m]:
                l = l+1
            else:
                # m --> r sorted
                if target < nums[m] or nums[r] < target:
                    r = m-1
                else:
                    l = m+1
         
            m = (l+r+1) // 2
            print(m)

        return False