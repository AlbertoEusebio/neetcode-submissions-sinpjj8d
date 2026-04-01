class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dp = defaultdict(int)

        for n in nums:
            dp[n]+=1

            if dp[n]>1:
                return True

        return False