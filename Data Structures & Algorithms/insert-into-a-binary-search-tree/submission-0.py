# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            v = self.insertIntoBST(root.left, val)
            root.left = v if v else None
        else:
            v = self.insertIntoBST(root.right, val)
            root.right = v if v else None

        return root