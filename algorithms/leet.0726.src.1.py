class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stk = [Counter()]
        n = len(formula)
        i = 0
        while i < n:
            c = formula[i]
            if c == '(':
                stk.append(Counter())
                i += 1
            elif c == ')':
                d = stk.pop()
                i += 1
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                k = int(formula[i:j] or 1)
                for x, v in d.items():
                    stk[-1] += Counter({x: v * k})
                i = j
            else:
                j = i
                while j < n and formula[j].isalnum():
                    j += 1
                # print(formula[i:j])
                for it in re.finditer(r'([A-Z][a-z]*)(\d*)', formula[i:j]):
                    x, c = it.groups()
                    # print(x, c or 1)
                    stk[-1] += Counter({x: int(c or 1)})
                i = j
        # print(stk)
        # while len(stk) > 1:
        #     stk[-1] += stk.pop()
        return ''.join([f'{k}{v if v > 1 else ""}' for k, v in sorted(stk[-1].items())])
