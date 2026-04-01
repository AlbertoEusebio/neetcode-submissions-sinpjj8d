class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # ij
        # dvabcdfk

        #    i  j
        # dvabcafk


        #  ij
        # bbbbbbbb

        if len(s) < 1:
            return 0

        i, j = 0, 0

        window = set()
        max_len = 0

        while j < len(s):
            print(window)
            if len(window) > max_len:
                max_len = len(window)
            if s[j] not in window:
                window.update(s[j])
            else:
                while i < j and s[i] != s[j]:
                    window.remove(s[i])
                    i += 1
                # window.remove(s[j])
                i += 1
            j += 1
        
        if len(window) > max_len:
            max_len = len(window)

        return max_len
            