# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)
        return list(dfs(root))
