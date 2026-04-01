class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,0
        s=0
        mlen = -1
        while j<= len(nums):

            if s < target:
                if j == len(nums):
                    break
                s+= nums[j]
                j+=1
            elif s >= target:
                if mlen == -1 or j-i < mlen:
                    mlen = j-i
                # print(nums[i:j],i,j, j-i, s)
                s-=nums[i]
                i+=1

        return max(mlen,0)