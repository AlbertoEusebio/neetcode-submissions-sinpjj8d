class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ''
        for c in s:
            if c.isalnum():
                a += c.lower()
        print(a)
        return a == a[::-1]