class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        n = len(nums)

        print(nums)

        ret = []

        for k in range(n-2):
            if nums[k] > 0:
                break
            if k>0 and nums[k] == nums[k-1]:
                continue
            
            i = k+1
            j = n-1
            while i < j:
                s = nums[i] + nums[j] + nums[k]
                # print(k, i, j, s)
                if s == 0:
                    ret.append([nums[k], nums[i], nums[j]])
                    # both numbers because the sum with 2 equal numbers (k, i or j) by default wants number j or i so we would have a dup
                    j -=1
                    i +=1
                    while i<j and nums[i] == nums[i-1]:
                        i += 1 # we do not want dup
                elif s > 0:
                    j -=1
                else:
                    i +=1
        
        return ret