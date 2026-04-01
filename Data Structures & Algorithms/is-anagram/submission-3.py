class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dp = defaultdict(int)

        for c in s:
            dp[c]+=1

        for c in t:
            dp[c]-=1
            if dp[c] < 0:
                return False

        for c,v in dp.items():
            if v != 0:
                return False

        return True