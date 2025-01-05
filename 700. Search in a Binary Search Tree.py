# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def BST(root):
            if not root:
                return
            if val == root.val:
                return root
            elif val < root.val:
                return BST(root.left)
            else:
                return BST(root.right)
        return BST(root)