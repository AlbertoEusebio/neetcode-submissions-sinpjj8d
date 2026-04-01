class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) -1

        while l < r:
            m = (l+r) // 2

            if nums[m] < nums[r]:
                r = m
            elif nums[m] >= nums[l]:
                l = m + 1

        print(l)
        pivot = l # k is the pivot element

        if target <= nums[-1]:
            i, j = pivot, len(nums) -1
        elif target >= nums[0]:
            i, j = 0, pivot
        else:
            i= -1
            j=-1

        # print(i, j)
        k = (i+j) // 2

        while i < j:
            print(i, k, j)

            if nums[k] < target:
                 i = k+1
            elif nums[k] > target:
                j = k-1
            else:
                return k

            k = (i+j) // 2

        print(i, k, j)

        if nums[k] == target:
            return k

        return -1