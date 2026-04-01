from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.keys[key]

        values = []
        timestamps = []
        for v, t in vals:
            values.append(v)
            timestamps.append(t)

        print(timestamps)

        l,r = 0, len(timestamps) - 1
        
        max_m = None
        while l <= r:

            m = (l + r) // 2

            if timestamps[m] == timestamp:
                return values[m]

            if timestamps[m] > timestamp:
                r = m - 1
            else:
                if not max_m or timestamps[max_m] < timestamps[m]:
                    max_m = m  
                l = m + 1

        print(max_m)
        return values[max_m] if max_m is not None else ""