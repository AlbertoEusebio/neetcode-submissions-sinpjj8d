class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        res = ""
        for i in range(min(m, n), 0, -1):
            res = str1[:i]
            if len(str1) % i != 0 or len(str2) % i != 0:
                continue

            print(res, i)

            a, b = m // i, n // i

            if res * a == str1 and res * b == str2:
                return res
        return ""
