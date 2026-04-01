class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = 0
        b = 0

        if num1 == '0' or num2 == '0':
            return '0'

        for i,n in enumerate(num1[::-1]):
            a += int(n) * (10**i)
        
        for i,n in enumerate(num2[::-1]):
            b += int(n) * (10**i)
        
        print(a, b)

        c = a * b

        s = ""
        while c > 0:
            s += str(c%10)
            c = c // 10

        return s[::-1]