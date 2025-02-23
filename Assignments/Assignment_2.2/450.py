# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None

            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            successor = self.find_min(root.right)
            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)
        return root

    def find_min(self, root: TreeNode):
        while root.left:
            root = root.left
        return root