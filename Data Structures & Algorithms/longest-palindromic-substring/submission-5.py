class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # DFS at each step can increase i or decrease j

        palindrome = set()

        def is_pal(st):

            if st in palindrome:
                return True

            if st == st[::-1]:
                palindrome.add(st)
                return True
            return False

        if len(s) == 1:
            return s

        # sweep lenghts
        for l in range(len(s), 0, -1):
            print(l)
            for i in range(0, len(s)-l+1):
                if is_pal(s[i:i+l]): 
                    return s[i:i+l]
