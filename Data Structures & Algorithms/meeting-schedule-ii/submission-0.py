"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([t.start for t in intervals])
        ends = sorted([t.end for t in intervals])

        i, j = 0,0
        n = len(intervals)
        count = 0
        m= 0
        while i<n and j<n:
            if starts[i] >= ends[j]:
                count -= 1
                j+=1
            if starts[i] < ends[j]:
                count += 1

                if count > m:
                    m=count
                i+=1

        return m
          
