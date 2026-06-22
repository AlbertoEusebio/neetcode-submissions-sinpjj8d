"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        que = []
        heapq.heapify(que)

        for c in intervals:
            heapq.heappush(que, (c.start, 1))
            heapq.heappush(que, (c.end, -1))

        max_overlap = 0
        count = 0

        while que:
            s, v = heapq.heappop(que)

            count += v
            max_overlap = max(max_overlap, count)

        return max_overlap