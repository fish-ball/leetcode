# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = {}
        def dfs(nd, h, dt):
            if not nd:
                return
            if h not in d:
                d[h] = []
            d[h].append((dt, nd.val))
            dfs(nd.left, h-1, dt+1)
            dfs(nd.right, h+1, dt+1)
        dfs(root, 0, 0)
        ans = []
        for k in sorted(d.keys()):
            ans.append([y for x, y in sorted(d[k])])
        return ans
