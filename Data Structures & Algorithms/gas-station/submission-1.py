class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        def dfs(i, t, visited):
            print(i)
            if visited[i] == 1:
                return i

            t += gas[i]
            visited[i] = 1
            if cost[i] > t:
                return -1
            
            return dfs((i+1) % len(gas), t-cost[i], visited)


        visited = [0] * len(gas)

        for i in range(len(gas)):
            a = dfs(i, 0, visited.copy())
            if a != -1:
                return a

        return -1