class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        n = columnNumber

        # N - 26 < 0:

        while n > 0:
            is_z = n % 26 == 0
            res += chr(ord('A') + n % 26 - 1) if not is_z else 'Z'
            n -= n % 26 if not is_z else 26
            n = n // 26
        return res[::-1]