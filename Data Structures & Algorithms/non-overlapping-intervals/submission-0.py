class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)

        print(intervals)

        res = 0

        s, e = intervals[0]
        taken = 1
        for t in intervals[1:]:
            si, ei = t

            if si < e:
                # overlap --> exclude overlapping 
                e = min(e, ei)
            else:
                # no overlap
                e = ei
                taken += 1

        return len(intervals) - taken
