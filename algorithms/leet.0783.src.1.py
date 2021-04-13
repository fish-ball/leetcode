# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans = None
        last = None
        def dfs(node):
            if not node:
                return
            nonlocal last, ans
            dfs(node.left)
            if last is not None:
                diff = abs(node.val - last)
                ans = diff if ans is None else min(ans, diff)
            last = node.val
            dfs(node.right)

        dfs(root)
        return ans

