# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, val):
            if not root:
                return 0
            val += root.val
            x = 0
            if val == targetSum:
                x += 1
            x+=dfs(root.left, val)
            x+=dfs(root.right, val)
            return x

        res = 0
        stack = []
        if root:
            stack = [root]

        while stack:
            current = stack.pop()
            res += dfs(current, 0)

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        return res