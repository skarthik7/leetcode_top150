"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        visited = {}

        def clone(node):
            if node in visited:
                return visited[node]
            clone_node = Node(node.val, [])
            visited[node] = clone_node
            if node.neighbors:
                clone_node.neighbors = [clone(n) for n in node.neighbors]
            return clone_node


        return clone(node)