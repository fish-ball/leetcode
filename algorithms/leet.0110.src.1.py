# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def h(nd):
            return 0 if not nd else max(h(nd.left), h(nd.right))+1
        return abs(h(root.left)-h(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
