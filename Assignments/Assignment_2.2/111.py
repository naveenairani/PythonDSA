# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        def dfs(node, level):
            if not node:
                return
            if level > len(res):
                res.append([node.val, 1])
            else:
                res[level-1][0] += node.val
                res[level-1][1] += 1
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root, 1)
        return [i[0] / i[1] for i in res]