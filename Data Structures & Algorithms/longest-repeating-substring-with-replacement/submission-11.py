class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = defaultdict(int)

        l = 0
        max_len = 0
        maxf = 0

        for r in range(len(s)):
            freq[s[r]] += 1 # update current char freq
            maxf = max(freq[s[r]], maxf)

            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1

            max_len = max(max_len, r -l +1)

        return max_len
