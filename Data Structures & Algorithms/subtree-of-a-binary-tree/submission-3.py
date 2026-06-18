# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(r, s):

            if r is None and s is None:
                return True
            elif None in [r, s]:
                return False

            if r.val != s.val:
                return False
            
            # compare
            return dfs(r.left, s.left) and dfs(r.right, s.right)
        
        if root is None and subRoot is None:
            return True
        elif root is None:
            return False

        if dfs(root, subRoot):
            return True

        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)