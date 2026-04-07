import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        tsk = [(t[0], t[1], i) for i,t in enumerate(tasks)]
        avail = []
        heapq.heapify(tsk)
        heapq.heapify(avail)

        res = []
        t = 0
        while tsk or avail:
            # pull available tasks
            while tsk and tsk[0][0] <= t:
                s, p, i = heapq.heappop(tsk)
                heapq.heappush(avail, (p, s, i))
            
            if len(avail) == 0:
                    s, p, i = heapq.heappop(tsk)
                    heapq.heappush(avail, (p, s, i))
                    t = s
            p, s, i = heapq.heappop(avail)
            t += p
            # print(t)
            res.append(i)

        return res