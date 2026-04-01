class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        nodes = {}

        for i in range(n):
            nodes[i] = []

        for flight in flights:
            fm, to, p = flight
            nodes[fm].append((to, p))

        print(nodes)

        # Traverse the graph untill you reach the dst
        # then select shortest path

        res = []

        def dfs(n, path, k, visited):
            fm, c = n

            if fm == dst:
                path.append((fm, c))
                visited[fm] = 1
                res.append(path.copy())
                path.pop()
                return
            elif visited[fm]:
                return
            elif k == 0:
                return
            
            path.append((fm, c))
            visited[fm] = 1

            for n in nodes[fm]:
                dfs(n, path, k-1, visited)

            path.pop()
            visited[fm] =0
            return

        dfs((src, 0), [], k+1, [0]*n)


        min_len = []
        for re in res:
            l = sum(r[1] for r in re)
            min_len.append(l)

        return min(min_len) if min_len else -1