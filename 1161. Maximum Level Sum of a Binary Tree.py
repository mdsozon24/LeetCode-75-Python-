# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        bfs = []
        if not root:
            return 0
        l = []
        l.append(root)
        while len(l)>0:
            n = len(l)
            crr = []
            for i in range(n):
                c = l.pop(0)
                crr.append(c.val)
                if c.left :
                    l.append(c.left)
                if c.right :
                    l.append(c.right)
            bfs.append(crr)
        a = [sum(j) for j in bfs]
        return a.index(max(a))+1