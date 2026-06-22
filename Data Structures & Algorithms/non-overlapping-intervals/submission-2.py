import heapq

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)

        e0 = None
        ret = 0

        for s, e in intervals:
            if e0 is None or s >= e0:
                e0 = e
            else:
                e0 = min(e0, e)
                ret += 1

        return ret