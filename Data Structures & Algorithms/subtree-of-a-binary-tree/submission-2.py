# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(ra, rb):
            if not ra and not rb:
                return True
            elif not ra or not rb:
                return False
    
            if ra.val != rb.val:
                return False

            left = sameTree(ra.left, rb.left)
            right = sameTree(ra.right, rb.right)

            return left and right

        if not root:
            return False

        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
