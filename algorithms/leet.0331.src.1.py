class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if preorder == '#':
            return True
        elif preorder.startswith('#'):
            return False
        seq = preorder.split(',')
        node = [seq[0]]
        path = [node]

        def sharp():
            # print('Sharp')
            nonlocal node
            if not node or len(node) >= 3:
                return False
            node.append('#')
            if len(node) == 3:
                path.pop()
                # print('Pop', path)
                node = path[-1] if path else None
                if node:
                    node.pop()
                    return sharp()
            return True


        for c in seq[1:]:
            # print(path)
            if not node:
                return False
            if c == '#':
                if not sharp():
                    return False
            else:
                old = node
                node = [c]
                old.append(c)
                path.append(node)
        
        return node is None


