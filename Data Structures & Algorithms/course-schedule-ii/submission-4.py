from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        nodes = {}
        
        for i in range(numCourses):
            graph[i] = []
            nodes[i] = []

        for pre in prerequisites:
            a, b = pre
            nodes[a].append(b) # prequisites
            graph[b].append(a) # ordering of unlocking
        
        # BFS from the nodes with less/more prequisites?
        # [a] --> [e, f, g, h, i] 
        # [e] --> [a, b, c, d]

        # the roots are the nodes who are not prequisites to any else

        print(graph)
        print(nodes)

        que = deque()

        # put in frontier ALL the roots
        for n, v in nodes.items():
            if v == []:
                que.append(n)

        path = []

        while que:
            n = que.popleft()
            if n not in path:
                path.append(n)
            else:
                continue

            for pre in graph[n]:
                nodes[pre].remove(n) # visited
            
            # put in frontier ALL the roots
            for n, v in nodes.items():
                if v == []:
                    que.append(n)


        # put in frontier ALL the roots
        for n, v in nodes.items():
            if v != []:
                return []

        return path
