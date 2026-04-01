from collections import defaultdict
import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occur = [0] * 26

        # 4 char
        # 2 dist
        # n = 2

        char_occ = []

        s = 0
        for t in tasks:
            occur[ord(t) - ord('A')] += 1
            s += 1

        for i, o in enumerate(occur):
            if o != 0:
                char_occ.append((-o, chr(i + ord('A'))))


        heapq.heapify(char_occ)
        print(char_occ)

        que = deque([])

        t = 0
        while char_occ or que:
            t += 1

            print(t, char_occ)
            print(t, que)
            if char_occ:
                k, c = heapq.heappop(char_occ)
                k = k + 1
                if k != 0:
                    que.append(((k, c), t + n))

            print(t, char_occ)
            print(t, que)

            # Time check
            while que and que[0][1] <= t:
                x, _ = que.popleft()
                heapq.heappush(char_occ, x)

        return t
