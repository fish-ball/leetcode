"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        return 0 if not root else max([self.maxDepth(x)+1 for x in root.children]) if root.children else 1
