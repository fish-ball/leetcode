# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        p = []
        def dfs(node, acc=0):
            if not node:
                return 0
            p.append(node.val)
            acc += node.val
            ac = acc
            ans = 0
            for x in p:
                if ac == targetSum:
                    ans += 1
                ac -= x
            ans += dfs(node.left, acc)
            ans += dfs(node.right, acc)
            p.pop()
            return ans
        return dfs(root)
