import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        h = []
        freqs =defaultdict(int)
        heapq.heapify(list(set(nums)))

        while len(nums):
            n = nums.pop()
            if n not in freqs:
                heapq.heappush(h, n)
            freqs[n] += 1

        while h:
            n = heapq.heappop(h)
            while freqs[n] != 0:
                freqs[n] -= 1
                nums.append(n)
        return nums