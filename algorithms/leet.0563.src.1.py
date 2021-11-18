# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        ans = 0
        def dfs(nd):
            nonlocal ans
            if not nd:
                return 0
            a = dfs(nd.left)
            b = dfs(nd.right)
            ans += abs(a-b)
            return a+b+nd.val
        dfs(root)
        return ans
