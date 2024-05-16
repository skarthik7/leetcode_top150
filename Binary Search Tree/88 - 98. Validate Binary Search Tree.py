# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if not lower < node.val < upper:
                return False
            return isValid(node.left, lower, node.val) and isValid(node.right, node.val, upper)

        return isValid(root)