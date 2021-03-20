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
                    abs(a) // abs(b) * (-1 if (a<0)^(b<0) else 1) if s == '/' else None
                )
            else:
                stk.append(int(s))
            # print(stk)
        return stk.pop()
