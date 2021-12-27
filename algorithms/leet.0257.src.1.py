# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []
        path = []
        def dfs(nd):
            if not nd:
                return
            path.append(str(nd.val))
            if not nd.left and not nd.right:
                ans.append('->'.join(path))
            if nd.left:
                dfs(nd.left)
            if nd.right:
                dfs(nd.right)
            path.pop()
        dfs(root)
        return ans
                
