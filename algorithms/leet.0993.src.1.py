# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        p1 = None
        h1 = -1
        p2 = None
        h2 = -1
        def dfs(node, depth=0, parent=None):
            nonlocal p1, h1, p2, h2
            # print(f'dfs({node and node.val}, {depth})')
            if not node:
                return
            if node.val == x:
                h1 = depth
                p1 = parent
            if node.val == y:
                h2 = depth
                p2 = parent
            dfs(node.left, depth+1, node)
            dfs(node.right, depth+1, node)
        dfs(root)
        # print(h1, h2, p1, p2)
        return h1==h2 and p1 and p2 and p1!=p2
