class Solution:
    def getSum(self, a: int, b: int) -> int:
        

        def setBit(val, st, idx):
            mask = 1 << idx
            return (val | mask) if st else (val & ~mask)

        def getBit(val, idx):
            return (val >> idx) & 1

        carry = 0
        s = 0

        for i in range(32):
            ai = getBit(a, i)
            bi = getBit(b, i)
            print(bin(s),ai, bi, ai ^ bi ^ carry)
            s = setBit(s, ai ^ bi ^ carry, i)
            carry = (ai & bi) | (ai & carry) | (bi & carry)
        
        if s > 0x7FFFFFFF:
            s = ~(s ^ ((2 ** 32) - 1))

        print(bin(a))
        print(bin(b))
        print(bin(s))

        return s