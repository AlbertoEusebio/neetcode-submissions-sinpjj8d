class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        mn, mx = 1,1

        for n in nums:
            if n == 0:
                mn,mx = 1,1

            tmp = mx * n
            mx = max(tmp, mn * n, n)
            mn = min(tmp, mn*n, n)
            res = max(mx, res)

        return res
