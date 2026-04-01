class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dp = defaultdict(int)

        for n in nums:
            dp[n]+=1

        res = list()
        for k, v in dp.items():
            if v > len(nums) // 3:
                res.append(k)
        return res