class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find pivot --> same thing as minimum

        l, r = 0, len(nums)-1
        m = (l+r)//2

        if len(nums) == 1:
            return nums[0]
        elif nums[l] < nums[r]:
            return nums[l]
        elif nums[r] < nums[l] and nums[r] < nums[r-1]:
            return nums[r]


        while l <= r:
            print(l, r, m)
            if nums[m] < nums[m-1]:
                # pivot
                return nums[m]
            if nums[m] > nums[r]:
                # pivot on rght
                l = m + 1
            elif nums[m] < nums[r]:
                # pivot on the left
                r = m - 1

            m = (l + r) // 2
