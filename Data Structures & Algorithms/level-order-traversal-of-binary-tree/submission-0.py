# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # BFS
        levels = []

        if root:
            queue = deque([(root,1)])
        else:
            return levels

        while queue:
            p, d = queue.popleft()

            if len(levels) < d:
                levels.append([])
            
            levels[d-1].append(p.val)

            print(p.val, d)
            if p.left:
                queue.append((p.left, d+1))
            if p.right:
                queue.append((p.right, d+1))

        return levels
