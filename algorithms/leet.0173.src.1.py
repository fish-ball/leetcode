# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        def dfs(node):
            if node.left:
                yield from dfs(node.left)
            yield node.val
            if node.right:
                yield from dfs(node.right)
        self.iter = dfs(root)
        try:
            self.buf = next(self.iter)
        except:
            self.buf = None

    def next(self) -> int:
        buf = self.buf
        try:
            self.buf = next(self.iter)
        except:
            self.buf = None
        return buf

    def hasNext(self) -> bool:
        return self.buf is not None



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
