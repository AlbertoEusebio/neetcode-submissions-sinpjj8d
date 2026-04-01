# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # BFS
    
        levels = []

        if not root:
            return []
        queue = deque([(root, 1)])

        while queue:

            p, d = queue.popleft()
            if len(levels) < d:
                levels.append([])

            print(p.val)

            levels[d-1].append(p.val)

            if p.left:
                queue.append((p.left, d+1))
            if p.right:
                queue.append((p.right, d+1))

        visible = []

        for l in levels:
            visible.append(l[-1])

        return visible