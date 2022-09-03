# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        @lru_cache(None)
        def calc(node):
            nonlocal ans
            if not node:
                return 0, 0
            n1, s1 = calc(node.left)
            n2, s2 = calc(node.right)
            n = n1 + n2 + 1
            s = s1 + s2 + node.val
            if node.val == s // n:
                # print('>>', node.val)
                ans += 1
            return n, s
        calc(root)
        return ans
