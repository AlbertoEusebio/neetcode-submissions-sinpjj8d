from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        ret = []

        for n in nums:
            freq[n] += 1

        ret = [k for k,v in sorted(freq.items(), key=lambda item: item[1], reverse=True)[:k]]

        return ret