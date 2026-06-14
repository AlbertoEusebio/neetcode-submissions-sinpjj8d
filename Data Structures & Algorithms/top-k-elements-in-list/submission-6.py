import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        que = []
        heapq.heapify(que)

        for n in nums:
            freq[n] += 1

        for n,f in freq.items():
            heapq.heappush(que, (-f, n))
        
        ret = []
        for i in range(k):
            _, n = heapq.heappop(que)
            ret.append(n)

        return ret
