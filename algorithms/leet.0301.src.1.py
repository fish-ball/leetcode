class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def side_process(s):
            n = len(s)
            q = set([''])
            for c in s:
                qq = set()
                if c == ')':
                    for ss in q:
                        acc = 0
                        for i, cc in enumerate(ss):
                            if ss[i] == '(':
                                acc += 1
                            elif ss[i] == ')':
                                acc -= 1
                        if acc > 0:
                            qq.add(ss + ')')
                            continue
                        ss += ')'
                        for i, cc in enumerate(ss):
                            if cc == ')':
                                qq.add(ss[:i] + ss[i+1:])
                    q = qq
                else:
                    q = set(ss + c for ss in q)
                # print(q)
            return q
        ans = set()
        def rev(s):
            return ''.join({')': '(', '(': ')'}.get(c, c) for c in s[::-1])
        # print(side_process(rev(s)))
        for ss in side_process(rev(s)):
            # print(ss, side_process(rev(ss)))
            ans |= side_process(rev(ss))
        return list(ans)
