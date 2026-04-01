from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        # Pacific: i < 0 or j < 0
        # Atlantic: i >= len(heights) or j >= len(heights)
        # this is a DFS problem: start from border nodes and climb up
        # we stop at the sinks and return their coords --> sinks for PAC & ATL 
        # are the ones to consider
  
        res = []
        sinks_pac = set()
        sinks_atl = set()

        def dfs(i, j, visited, prev):
            if i < 0 or i >= len(heights) or j < 0 or j>=len(heights[0]):
                return
            elif (i,j) in visited or heights[i][j] < prev:
                return

            visited.add((i, j))

            dfs(i+1, j, visited, heights[i][j])
            dfs(i-1, j, visited, heights[i][j])
            dfs(i, j+1, visited, heights[i][j])
            dfs(i, j-1, visited, heights[i][j])

        # PAC
        for i in range(len(heights)):
            dfs(i, 0, sinks_pac, heights[i][0])
        for j in range(len(heights[0])):
            dfs(0, j, sinks_pac, heights[0][j])        
        
        # ATL
        for i in range(len(heights)):
            dfs(i, len(heights[0]) - 1, sinks_atl, heights[i][len(heights[0]) - 1])
        for j in range(len(heights[0])):
            dfs(len(heights) - 1, j, sinks_atl, heights[len(heights) - 1][j])

        print(sorted(sinks_pac), sorted(sinks_atl))

        return list(set(sinks_pac).intersection(set(sinks_atl)))