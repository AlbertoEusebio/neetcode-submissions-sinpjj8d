class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)

        for acc in accounts:
            # print(acc)
            a = acc[0]
            mails = acc[1:]
            for i,m in enumerate(mails):
                graph[m] += mails[:i]
                graph[m] += mails[i+1:]

        print(graph)
        
        res = []
        visited = set()

        for acc in accounts:
            a = acc[0]
            visit = set()

            que = deque([])
            
            mails = acc[1:]
            for m in mails:
                if m not in visit:
                    visit.add(m)
                    que.append(m)

            if len(visited.intersection(visit)) > 0:
                print(visited)
                continue

            while que:
                l = que.popleft()

                mails = graph[l]
                for m in mails:
                    if m not in visit:
                        visit.add(m)
                        que.append(m)
            
            for v in visit:
                visited.add(v)
            
            res.append([a] + list(visit))
        return res