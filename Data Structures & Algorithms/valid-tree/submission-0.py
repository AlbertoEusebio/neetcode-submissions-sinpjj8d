class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        nodes = {}

        for i in range(n):
            nodes[i] = []

        for e in edges:
            i, j = e
            nodes[i].append(j)
            nodes[j].append(i)
        
        # a valid tree doesn't have self loops
        # dfs over the tree keeping an array of visited nodes
        # at each step always go to leaves, parent is excluded
        # being undirected, it doesn't matter where u start
        # a - b - e
        #   - c
        #   - d - o

        # c - a - b - e
        #       - d - o


        def dfs(i, parent, visited):

            if visited[i]:
                return False

            visited[i] = 1

            loops = []
            for j in nodes[i]:
                if j != parent:
                    loops.append(dfs(j, i, visited))

            return all(loops)

        visited = [0] * n

        a = dfs(0, -1, visited)

        if not a or sum(visited) != n:
            return False
        return True

