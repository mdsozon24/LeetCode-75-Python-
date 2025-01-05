# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def Bfs(root):
            nonlocal ans
            if not root:
                return ans
            que = []
            que.append(root)
            while len(que)!=0:
                crr = []
                for i in range(len(que)):
                    c = que.pop(0)
                    crr.append(c.val)
                    if c.left:
                        que.append(c.left)
                    if c.right:
                        que.append(c.right)
                ans.append(crr)
        Bfs(root)
        res = []
        for n in ans:
            res.append(n[-1])
        return res