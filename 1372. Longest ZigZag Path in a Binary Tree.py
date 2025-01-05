# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_len = 0
        def dfs(root,stp,go):
            nonlocal max_len
            if not root:
                return 
            max_len = max(max_len,stp)
            if go:
                dfs(root.left,stp+1,False)
                dfs(root.right,1,True)
            else:
                dfs(root.right,stp+1,True)
                dfs(root.left,1,False)
        dfs(root.left,1,False)
        dfs(root.right,1,True)
        return max_len