# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        class DiameterData:
            def __init__(self, diameter, height):
                self.diameter = diameter
                self.height = height

        def calculateDiameterAndHeight(root: Optional[TreeNode]) -> DiameterData:
            if not root:
                return DiameterData(0, 0)

            leftData = calculateDiameterAndHeight(root.left)
            rightData = calculateDiameterAndHeight(root.right)

            currentDiameter = max(leftData.height + rightData.height,
                                  max(leftData.diameter, rightData.diameter))
            currentHeight = max(leftData.height, rightData.height) + 1

            return DiameterData(currentDiameter, currentHeight)

        data = calculateDiameterAndHeight(root)
        return data.diameter

        
   