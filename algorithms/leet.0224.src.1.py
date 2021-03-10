class Solution:
    def calculate(self, s: str) -> int:
        stk = []

        s = s.replace(' ', '')

        def commit():
            # print('commit', stk)
            if len(stk) < 3:
                return
            if stk[-2] == '+':
                x = stk.pop()
                stk.pop()
                stk[-1]  += x
            elif stk[-2] == '-':
                x = stk.pop()
                stk.pop()
                stk[-1]  -= x
            
        for i, c in enumerate(s):
            if c in '(+':
                stk.append(c)
            elif c == '-':
                if not stk or type(stk[-1]) != int:
                    stk.append(0)
                stk.append(c)
            elif c.isdigit():
                if stk and type(stk[-1]) == int:
                    stk[-1] *= 10
                    stk[-1] += int(c)
                else:
                    stk.append(int(c))
                if i == len(s) - 1 or not s[i+1].isdigit():
                    commit()
            elif c == ')':
                stk[-1] = stk.pop()
                commit()
            # print(c, stk)
            
        return stk[-1]
