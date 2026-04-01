"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        def dfs(node, copy, visited):

            if node is None or node in visited:
                return

            print(node, node.val)

            # copy.val = node.val
            visited[node] = copy

            neighbors = []
            for n in node.neighbors:
                if n in visited:
                    cn = visited[n]
                else:
                    cn = Node(n.val)
                neighbors.append(cn)
                dfs(n, cn, visited)

            copy.neighbors = neighbors
            print(copy, copy.val, [n.val for n in copy.neighbors])

        if not node:
            return None

        visited = {}
        root = Node(node.val)
        dfs(node, root, visited)

        return root