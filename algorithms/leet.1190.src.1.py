class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = ['']
        for c in s:
            if c == '(':
               stk.append('')
            elif c == ')':
               t = stk.pop()[::-1]
               stk[-1] += t
            else:
               stk[-1] += c
            #print(stk)
        return stk[-1]
