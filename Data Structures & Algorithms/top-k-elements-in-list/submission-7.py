import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        que = []
        heapq.heapify(que)

        for n in nums:
            freq[n] += 1

        freq_bin = [list() for i in range(len(nums))]

        for n,f in freq.items():
            freq_bin[f-1].append(n) # create bucks of frequencies

        ret = []
        s=0
        for b in freq_bin[::-1]:
            c = len(b)
            if s + c >= k:
                return ret + b[:(k-s)]
            else:
                s += c
                ret = ret + b
            
        return ret
