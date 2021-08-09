# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        ans = []
        # 向下
        def dfs(node, n=0):
            if not node:
                return
            if n == k:
                ans.append(node.val)
                return
            dfs(node.left, n+1)
            dfs(node.right, n+1)
        dfs(target)
        # 向上
        def dfs2(node):
            if not node:
                return -1
            if node == target:
                return 1
            n1 = dfs2(node.left)
            if n1 > -1:
                if n1 == k:
                    ans.append(node.val)
                    return -1
                if n1 < k:
                    dfs(node.right, n1+1)
                return n1 + 1
            n2 = dfs2(node.right)
            if n2 > -1:
                if n2 == k:
                    ans.append(node.val)
                    return -1
                if n2 < k:
                    dfs(node.left, n2+1)
                return n2 + 1
            return -1
        dfs2(root)
        return ans
