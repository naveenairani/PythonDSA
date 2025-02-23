# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        stack_left = []
        stack_right = []

        curr = root
        
        while curr:
            stack_left.append(curr)
            curr = curr.left
        
        curr = root
        while curr:
            stack_right.append(curr)
            curr = curr.right

        smallest = stack_left[-1]
        largest = stack_right[-1]

        while smallest != largest:
            if smallest.val + largest.val == k:
                return True
            elif smallest.val + largest.val < k:
                curr = smallest.right
                while curr:
                    stack_left.append(curr)
                    curr = curr.left
                smallest= stack_left.pop()
            else:
                curr = largest.left
                while curr:
                    stack_right.append(curr)
                    curr = curr.right
                largest= stack_right.pop()
        return False