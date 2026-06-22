"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        seen = {}

        def clone(n):

            if n is None:
                return

            if n.val in seen:
                return seen[n.val]

            v = Node(n.val)
            seen[n.val] = v
 
            for ng in n.neighbors:
                v.neighbors.append(clone(ng))

            return v

        return clone(node) if node else None