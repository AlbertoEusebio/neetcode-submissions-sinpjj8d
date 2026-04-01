class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals, key=lambda x: x[0])

        s, e = intervals[0]

        res = []

        s, e = intervals[0]

        for t in intervals[1:]:
            si, ei = t
            if si > e:
                res.append([s,e])
                s = si
                e = ei
            elif si <= e:
                e = max(ei,e)

        res.append([s,e])
        return res
        
            
            