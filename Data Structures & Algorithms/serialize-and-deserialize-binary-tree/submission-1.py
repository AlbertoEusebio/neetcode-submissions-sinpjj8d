# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        serial = []
        
        def dfs(r):
            nonlocal serial
            
            if r is None:
                serial.append('null')
                return None
            
            serial.append(str(r.val))
            dfs(r.left)
            dfs(r.right)
        
        dfs(root)
        print(serial)
        return ','.join(serial)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        serial = data.split(',')[::-1]
        print(serial)

        j = 0
        def dfs(serial):
            c = serial.pop()

            if c == 'null':
                return None

            v = int(c)
            n = TreeNode(v)

            n.left = dfs(serial)
            n.right = dfs(serial)

            return n
        
        return dfs(serial)

