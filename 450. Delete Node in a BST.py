# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def bst(root,key):
            if not root:
                return
            if key > root.val :
                root.right = bst(root.right,key)
            elif key < root.val :
                root.left = bst(root.left,key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                
                crr = root.right
                while crr.left:
                    crr = crr.left
                root.val = crr.val
                root.right = bst(root.right,root.val)
            return root
        return bst(root,key)