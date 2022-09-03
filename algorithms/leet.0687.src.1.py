# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(nd):
            if not nd:
                return 0, 0
            a1 = 0
            a2 = 0
            b = 1
            if nd.left:
                aa, bb = dfs(nd.left)
                if nd.left.val == nd.val:
                    a1 = aa
                b = max(b, bb)
            if nd.right:
                aa, bb = dfs(nd.right)
                if nd.right.val == nd.val:
                    a2 = aa
                b = max(b, bb)
            b = max(b, a1 + a2 + 1)
            return 1 + max(a1, a2), b
        aaa, bbb = dfs(root)
        return max(bbb - 1, 0)
