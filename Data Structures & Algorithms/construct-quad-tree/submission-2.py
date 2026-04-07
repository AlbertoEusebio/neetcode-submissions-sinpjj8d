"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        if len(grid) == 1:
            return Node(grid[0][0], True)

        def dfs(i, j, w, h):
            print(i,j, w, h)

            if w == 2 and h == 2:
                # print(grid[i:i+h][j:j+w])
                s = 0
                for a in range(2):
                    for b in range(2):
                        s += grid[i+a][j+b]
                print("\t"*(len(grid)//w),i,j, w, h, s)
                
                if s != 4 and s != 0:
                    return Node(0, False, Node(grid[i][j], True), Node(grid[i][j+1], True), Node(grid[i+1][j], True), Node(grid[i+1][j+1], True))
                else:
                    v = 1 if s == 4 else 0
                    return Node(v, True, None, None, None, None)
            else:
                w_2, h_2 = w // 2, h // 2
                tl = dfs(i, j, w_2, h_2)
                tr = dfs(i, j+w_2, w_2, h_2)
                bl = dfs(i+h_2, j, w_2, h_2)
                br = dfs(i+h_2, j+w_2, w_2, h_2)
                s = sum([tl.val, tr.val, bl.val, br.val])

                if (s != 4 and s != 0) or (False in [tl.isLeaf, tr.isLeaf, bl.isLeaf, br.isLeaf]):
                    return Node(0, False, tl, tr, bl, br)
                else:
                    v = 1 if s == 4 else 0
                    return Node(v, True, None, None, None, None)

        return dfs(0, 0, len(grid[0]), len(grid))