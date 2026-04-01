class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def sumNum(na, nb):
            la = len(na)
            lb = len(nb)
            if la == 0:
                return nb
            elif lb == 0:
                return na

            na = na[::-1]
            nb = nb[::-1]

            l = max(len(na), len(nb))
            i = 0
            carry = 0
            sm = ""
            while i < la and i < lb:
                c = int(na[i]) + int(nb[i]) + carry
                carry = c // 10
                sm += str(c%10)
                i += 1

            while i < l:
                if l == la:
                    c = int(na[i]) + carry
                    carry = c // 10
                    sm += str(c%10)
                
                if l == lb:
                    c = int(nb[i]) + carry
                    carry = c // 10
                    sm += str(c%10)

                i += 1


            if carry:
                sm += str(carry)

            return sm[::-1]

        a = 0
        b = 0

        print(sumNum("222", "2220"))

        if num1 == '0' or num2 == '0':
            return '0'

        res = ""
        for i,n in enumerate(num1[::-1]):
            l = ""

            carry = 0
            for j,m in enumerate(num2[::-1]):
                c = int(m) * int(n) + carry
                carry = c // 10
                l += str(c%10)

            if carry:
                l += str(carry)

            l = l[::-1]

            l += '0'*i
            print(i, l, res)
            res = sumNum(l, res)
            print(i, l, res)
            

        return res