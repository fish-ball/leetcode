# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        def dfs(node):
            nonlocal ans
            if not node or ans:
                return 0
            k = dfs(node.left) | dfs(node.right) | \
                (1 if node==p else 2 if node==q else 0)
            if k == 3:
                ans = node
                return 0
            return k

        dfs(root)
        return ans
