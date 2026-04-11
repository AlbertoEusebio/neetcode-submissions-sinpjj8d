class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for eq, v in zip(equations, values):
            a, b = eq

            graph[a].append((b, v))
            graph[b].append((a, 1/v))
        
        res = []
        for eq in queries:
            a, b = eq
            if a not in graph or b not in graph:
                res.append(-1)
                continue

            que = deque([(a, 1)])
            visited = set(a)

            to_app = -1
            while que:
                c, v = que.popleft()

                if c == b:
                    to_app = v
                    break
            
                nodes = graph[c]
                for n in nodes:
                    if n[0] not in visited:
                        visited.add(n[0])
                        que.append((n[0], v * n[1]))
            res.append(to_app)
        return res 