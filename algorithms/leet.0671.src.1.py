# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(nd, val):
            if not nd:
                return -1
            if nd.val > val:
                return nd.val
            p = dfs(nd.left, val)
            q = dfs(nd.right, val)
            if p == -1:
                return q
            if q == -1:
                return p
            return min(p, q)
        return dfs(root, root.val)
