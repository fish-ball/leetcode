# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        def dfs(node, level=0):
            if not node:
                return
            if len(ans) < level + 1:
                ans.append([])
            ans[level].append(node.val)
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        dfs(root)
        return ans
