class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # first find pivot, then search target

        l, r= 0, len(nums)-1
        m = (l+r) // 2

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            return -1

        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r

        while l <= r:
            if nums[m] == target:
                return m
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
            
            m = (l+r) // 2

        pivot = m

        # print(pivot)
        if target == nums[pivot]:
            return pivot
        elif target > nums[-1]:
            l, r = 0, pivot - 1
        else:
            l, r = pivot + 1, len(nums)-1

        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r

        m = (l+r) // 2
        while l <= r:
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
            m = (l+r) // 2

        return -1
