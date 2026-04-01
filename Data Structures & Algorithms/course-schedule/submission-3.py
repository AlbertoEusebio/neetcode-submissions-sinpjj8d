class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # This is a problem of constructing the graph of prerequisites and then see if there is a loop

        nodes = {}

        for i in range(numCourses):
            nodes[i] = []

        for p in prerequisites:
            a, b = p
            nodes[a].append(b)

        print(nodes)

        visited = [0] * numCourses

        def dfs(n, visited):
            nonlocal nodes

            if visited[n]:
                return False

            visited[n] = 1

            no_loops = []
            for pre in nodes[n]:
                no_loops.append(dfs(pre, visited))

            print(visited)

            visited[n] = 0

            return all(no_loops) # all([]) -> True default, no prerequisites

        no_loops = []
        for i in range(numCourses):
            no_loops.append(dfs(i, visited))

        print(no_loops)

        return all(no_loops) 