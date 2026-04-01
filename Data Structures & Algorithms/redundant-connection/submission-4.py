from collections import defaultdict

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # union - find

        ranks = [1] * len(edges) # N edges
        parents = [i for i in range(len(edges))]

        for e in edges:
            i, j = e

            pi = parents[i-1]
            pj = parents[j-1]

            if pi == pj:
                return e

            if ranks[pi] >= ranks[pj]:
                ranks[pi] += ranks[pj]
                
                # constant time
                for p in range(len(parents)):
                    if parents[p] == pj:
                        parents[p] = pi
            else:
                ranks[pj] += ranks[pi]
                
                # constant time
                for p in range(len(parents)):
                    if parents[p] == pi:
                        parents[p] = pj
            
