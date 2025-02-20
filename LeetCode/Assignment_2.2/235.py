# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        self.dfs(root)
        # Find all ancestors of p
        ancestors = set()
        while p:
            ancestors.add(p)
            p = p.parent

        # Traverse ancestors of q and return the first one that is also an ancestor of p
        while q:
            if q in ancestors:
                return q
            q = q.parent

        return None
  

    def dfs(self, root, parent=None):
        if not root:
            return 

        root.parent = parent  # Set the parent pointer for the current node
        self.dfs(root.left, root)
        self.dfs(root.right, root)

        