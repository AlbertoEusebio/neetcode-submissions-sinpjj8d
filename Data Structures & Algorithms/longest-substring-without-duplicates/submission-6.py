class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        i, j = 0, 0
        max_l = 0
        window = set()

        while j < len(s):
            if s[j] not in window:
                window.add(s[j])
            else:   
                while s[i] != s[j] and i < j:
                    window.remove(s[i])
                    i += 1
                i += 1
                
                # widow.remove(s[i])
                # widow.add(s[j])
            # print(window, i, j)
            j += 1

            l = j - i
            max_l = max(l, max_l)

        return max_l 