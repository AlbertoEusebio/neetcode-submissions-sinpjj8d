class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

            start = 'JFK'
            nodes = defaultdict(list)
            visited = defaultdict(int)

            for t in tickets:
                s, e = t
                nodes[s].append(e)

            # sort
            for t in tickets:
                s, e = t
                nodes[s] = sorted(nodes[s])
                visited[(s, e)] += 1

            res = []
            path = []
            def dfs(s, path):
                print(path)
                if len(path) == len(tickets) + 1:
                    res.append(path)
                    return True
        
                children = nodes[s]

                for c in children:
                    if visited[(s, c)] > 0:
                        visited[(s, c)] -= 1
                        if dfs(c, path + [c]):
                            return True
                        visited[(s, c)] += 1
                
                return False

            dfs('JFK', ['JFK'])

            print(res)
            return res[0]