"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals = sorted(intervals, key=lambda l: l.start)

        t = -1
        for m in intervals:
            if t > m.start:
                return False
            
            t = m.end

        return True