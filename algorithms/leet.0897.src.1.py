# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        rt = TreeNode()
        nd = rt
        def dfs(node):
            nonlocal nd
            if not node:
                return
            dfs(node.left)
            nxt = node.right
            node.left = None
            node.right = None
            nd.right = node
            nd = nd.right
            dfs(nxt)
        dfs(root)
        return rt.right
