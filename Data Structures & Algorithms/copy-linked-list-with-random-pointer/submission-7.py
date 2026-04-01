"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

from collections import defaultdict

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        refs = defaultdict(list)
        nodes = []
        rand = []

        if not head:
            return None

        h = head
        while h != None:
            node = Node(h.val)
            print(node.val, h.random)
            refs[h] = node
            nodes.append(node)
            rand.append(h.random if h.random else None)
            h = h.next

        i = 0
        for i in range(len(nodes)-1):
            n = nodes[i]
            n.next = nodes[i+1]
            n.random = refs[rand[i]] if rand[i] is not None else None
        
        nodes[-1].next = None
        nodes[-1].random = refs[rand[-1]] if rand[-1] is not None else None

        return nodes[0] if len(nodes) > 0 else None
