class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        courses = defaultdict(list) # store prereq

        for a, b in prerequisites:
            courses[b].append(a)

        res = []
    
        for u,v in queries:
            que = deque([v])
            visited = set()

            r = False

            while que:
                n = que.popleft()

                if n == u:
                    r = True
                    break

                preq = courses[n]
                # print(n, preq)
                for p in preq:
                    if p not in visited:
                        visited.add(p)
                        que.append(p)

                
            res.append(r)
        
        return res