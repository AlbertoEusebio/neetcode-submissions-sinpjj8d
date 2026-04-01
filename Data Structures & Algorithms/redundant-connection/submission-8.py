from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # # union - find
        # ranks = [1] * len(edges) # N edges
        # parents = [i for i in range(len(edges))]

        # for e in edges:
        #     i, j = e

        #     pi = parents[i-1]
        #     pj = parents[j-1]

        #     if pi == pj:
        #         return e

        #     if ranks[pi] >= ranks[pj]:
        #         ranks[pi] += ranks[pj]
                
        #         # constant time
        #         for p in range(len(parents)):
        #             if parents[p] == pj:
        #                 parents[p] = pi
        #     else:
        #         ranks[pj] += ranks[pi]
                
        #         # constant time
        #         for p in range(len(parents)):
        #             if parents[p] == pi:
        #                 parents[p] = pj
            

        ## DFS
        # Here you use a dict to construct the graph
        nodes = defaultdict(list)

        for e in edges:
            i, j = e
            nodes[i].append(j)
            nodes[j].append(i)

        cycle = []
        cycle_start = -1

        def dfs(i, parent, visited):
            nonlocal cycle, cycle_start

            if visited[i]:
                cycle_start = i
                return True # unwind cycle

            visited[i] = 1

            for j in nodes[i]:
                if j == parent:
                    cyclestart = i
                    continue

                if dfs(j, i, visited):
                    if cycle_start != -1:
                        # Either Nodes or Edges. If Edges you must append also inverse
                        # nodes you can check if they are presente
                        # cycle.append([i, j])
                        # cycle.append([j, i])
                        cycle.append(j)
                    if i == cycle_start:
                        cycle_start = -1
                    return True

            return False

        visited = [0] * (len(edges)+1)

        dfs(1, -1, visited)

        print(cycle)

        for e in edges[::-1]:
            i, j = e
            if i in cycle and j in cycle:
                return e
        return []