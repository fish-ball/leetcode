class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for s in tokens:
            if s in '+-*/':
                b = stk.pop()
                a = stk.pop()
                stk.append(
                    a + b if s == '+' else
                    a - b if s == '-' else
                    a * b if s == '*' else
                    a // b if s == '/' else None
                )
            else:
                stk.append(int(s))
        return stk.pop()
