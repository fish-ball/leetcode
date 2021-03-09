class Solution:
    def removeDuplicates(self, S: str) -> str:
        stk = []
        for c in S:
            if stk and stk[-1] == c:
                stk.pop()
            else:
                stk.append(c)
            # print(c, stk)
        return ''.join(stk)
