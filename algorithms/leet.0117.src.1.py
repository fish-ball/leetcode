"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        path = []
        def dfs(node, k = 0):
            if not node:
                return None
            if k < len(path):
                path[k].next = node
                print(path[k].val, '>', node.val)
                path[k] = node
            else:
                path.append(node)
            dfs(node.left, k + 1)
            dfs(node.right, k + 1)
        dfs(root)
        return root
