class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        nodes = {}

        for i in range(n):
            nodes[i] = []

        for e in edges:
            i, j = e
            nodes[i].append(j)
            nodes[j].append(i) # so it doesn't matter
        
        visited = [0] * n

        def dfs(i, visited, color):
            if visited[i]:
                return

            visited[i] = color

            for j in nodes[i]:
                dfs(j, visited, color)

        
        color = 1
        for i in range(n):
            if not visited[i]:
                dfs(i, visited, color)
                color += 1

        print(visited)

        return len(set(visited))