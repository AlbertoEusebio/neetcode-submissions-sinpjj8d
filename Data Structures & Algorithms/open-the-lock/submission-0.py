from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        visited = set(deadends)
        que = deque([("0000", 0)])
    
        if "0000" in visited:
            return -1

        def children(state):
            children = []

            for i in range(4):
                # append state[i] + 1 and - 1
                # if state[i] == target[i]:
                #     continue

                ni = str((int(state[i]) + 1) % 10)
                children.append(state[:i] + ni + state[i+1:])

                ni = str((int(state[i]) - 1 + 10) % 10)
                children.append(state[:i] + ni + state[i+1:])
            return children

        # print((-8)%10)

        # min_steps = 200 * 4
        while que:
            res, s = que.popleft()
            # print(res, s)
            if res == target:
                print(res)
                return s
            cldrn = children(res)
            for c in cldrn:
                if c not in visited:            
                    visited.add(c)
                    que.append((c, s+1))
        return -1