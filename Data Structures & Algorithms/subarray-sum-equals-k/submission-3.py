class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = {0: 1}
        cum_sum = 0
        res = 0
        for n in nums:
            cum_sum += n

            diff = cum_sum - k
            res += dp.get(diff, 0) # if you get 0

            # the idea is cumsum[i] - cumsum[j] = k
            # so if cumsum - k is already visited, then the (i, j] subarray will sum to k
            # this is because the difference is imposed to be k
            # if the diff is not in the array, then up to this point there is no cumsum that can be subtracted to the current and gives j
            # duplicates are handled by the frequency
            dp[cum_sum] = 1 + dp.get(cum_sum, 0)

            # print(cum_sum, dp)

        return res