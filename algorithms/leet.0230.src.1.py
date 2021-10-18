# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(nd):
            nonlocal k
            if not nd: return None
            a = dfs(nd.left)
            if a is not None: return a
            k -= 1
            if not k: return nd.val
            return dfs(nd.right)
        return dfs(root)
