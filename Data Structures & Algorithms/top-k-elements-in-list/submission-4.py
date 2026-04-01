from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        buk = [list() for i in range(len(nums))]

        for ky, v in freq.items():
            buk[v - 1].append(ky)

        print(buk)
        ret = []

        for b in buk[::-1]:
            ret = ret + b
            print(ret, len(ret), k)
            if len(ret) >= k:
                return ret

        return ret