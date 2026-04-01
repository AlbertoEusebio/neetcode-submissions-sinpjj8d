class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1000
        # 0111
        # ....
        # 0000

        n = len(nums)
        b = (1 << len(nums)) - 1
        print(bin(b))

        t = 0
        for i in range(n+1):
            t ^= i

        x = 0
        for n in nums:
            x ^= n

        return t ^ x
        