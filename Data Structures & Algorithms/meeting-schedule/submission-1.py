"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals = sorted(intervals, key=lambda x: (x.start, x.end))

        e0 = None

        for c in intervals:
            s,e = c.start, c.end
            if e0 is None or s >= e0:
                e0 = e
            else:
                return False
        return True