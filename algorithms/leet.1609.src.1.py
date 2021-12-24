# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        odd = True
        while q:
            p = []
            for nd in q:
                if odd and not nd.val % 2 or not odd and nd.val % 2:
                    return False
                nd.left and p.append(nd.left)
                nd.right and p.append(nd.right)
            for i in range(1, len(p)):
                if odd and p[i].val >= p[i-1].val or \
                        not odd and p[i].val <= p[i-1].val:
                    return False
            odd = not odd
            q = p
        return True
