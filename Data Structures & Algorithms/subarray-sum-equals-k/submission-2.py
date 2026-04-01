class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = {0: 1}
        cum_sum = 0
        res = 0
        for n in nums:
            cum_sum += n

            diff = cum_sum - k
            res += dp.get(diff, 0)

            dp[cum_sum] = 1 + dp.get(cum_sum, 0)

            # print(cum_sum, dp)

        return res