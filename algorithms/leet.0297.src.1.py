# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        return f'{root.val}({self.serialize(root.left)},{self.serialize(root.right)})'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        k = data.find('(')
        node = TreeNode(int(data[:k]))
        data = data[k+1:-1]
        x = 0
        for i, c in enumerate(data):
            if c == '(':
                x += 1
            elif c == ')':
                x -= 1
            if not x and c == ',':
                break
        node.left = self.deserialize(data[:i])
        node.right = self.deserialize(data[i+1:])
        return node

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
