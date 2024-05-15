# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if node:
                inorder(node.left)
                if self.prev is not None:
                    self.min_diff = min(self.min_diff, node.val - self.prev.val)
                self.prev = node
                inorder(node.right)

        inorder(root)
        return self.min_diff