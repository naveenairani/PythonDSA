# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return Ture
        def areSymmetric(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif ((root1 is None)!=(root2 is None)) or root1.val != root2.val:
                return False
            else:
                return areSymmetric(root1.left, root2.right) and areSymmetric(root1.right, root2.left)
        return areSymmetric(root.left,  root.right)