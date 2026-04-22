class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 001
        # 100


        # 11111110101
        # 11111110110
        # 11111110111
        res = 0
        print(f"{left:>032b}\n{right:>032b}")
        for i in range(31, -1, -1):
            a = (left & (1 << i)) >> i
            b = (right & (1 << i)) >> i
            # print(f"{res:>0b}")
            if a != b:
                return res
            res |= (a & b) << i
        return res