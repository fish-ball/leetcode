# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(node):
            if not node:
                return
            yield from dfs(node.left)
            yield from dfs(node.right)
            yield node.val
        return list(dfs(root))
