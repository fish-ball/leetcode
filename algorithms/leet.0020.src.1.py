class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
                continue
            for x, y in zip(')]}', '([{'):
                if c == x:
                    if not stack or stack.pop() != y:
                        return False
        return not stack
