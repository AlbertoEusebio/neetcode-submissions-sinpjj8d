# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # DFS
        stack = deque([(root, root.val)])
        
        good = 0 # root always good

        while stack:
            n, m = stack.pop()

            # m is max val encountered in this path
            if n.val >= m:
                good += 1
                print(n.val)

            if n.right:
                stack.append((n.right, max(n.val, m)))
            if n.left:
                stack.append((n.left, max(n.val, m)))

        return good