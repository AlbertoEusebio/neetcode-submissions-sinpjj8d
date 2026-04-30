class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        if k == n:
            return max(nums)
        elif k == 1:
            return sum(nums)
        
        # binary search on the solution, linear check on arrays

        def check_sum(s):
            c = 0
            i = 1
            for n in nums:
                if c + n > s:
                    c = n
                    i += 1
                    if i > k:
                        return False
                else:
                    c+=n
            return True

        l = max(nums)
        r = sum(nums)

        res = r

        while l <= r:
            mid = (r+l)//2

            if check_sum(mid):
                res = mid
                r = mid -1
            else:
                l = mid+1

        return res