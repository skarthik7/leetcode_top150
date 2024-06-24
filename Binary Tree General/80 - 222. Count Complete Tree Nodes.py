# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.getDepth(root, True)
        right_depth = self.getDepth(root, False)
        
        if left_depth == right_depth:
            return (1 << left_depth) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    def getDepth(self, node: Optional[TreeNode], isLeft: bool) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.left if isLeft else node.right
        return depth