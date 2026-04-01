class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        triplets = []
        for k in range(len(nums)):
            if nums[k] > 0:
                break
            if k>0 and nums[k] == nums[k-1]:
                continue
            l, r = k+1, len(nums)-1
            while l < r:
                if nums[r] + nums[l] + nums[k] > 0:
                    r -= 1
                elif nums[r] + nums[l] + nums[k] < 0:
                    l += 1
                else:
                    triplets.append([nums[r], nums[l], nums[k]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return triplets