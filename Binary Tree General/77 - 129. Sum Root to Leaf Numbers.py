# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)

    def helper(self, root, current_sum):
        if not root:
            return 0
        current_sum = current_sum * 10 + root.val
        if not root.left and not root.right:
            return current_sum
        return self.helper(root.left, current_sum) + self.helper(root.right, current_sum)