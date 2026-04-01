class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        res = []
        
        n = len(nums)
        for i in range(n):

            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, n):

                if j>i+1 and nums[j] == nums[j-1]:
                    continue

                l, r = j+1, n-1
                while l<r:
                    t = nums[i]+nums[j]+nums[l]+nums[r]
                    if t == target:
                        if [nums[i], nums[j], nums[l], nums[r]] not in res:
                            res.append([nums[i], nums[j], nums[l], nums[r]])
                    if t > target:
                        r-=1
                    else:
                        l+=1

        return res