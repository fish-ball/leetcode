class Solution:
    def checkValidString(self, s: str) -> bool:
        mx = 0
        mn = 0
        for c in s:
            if c == '(':
                mx += 1
                mn += 1
            elif c == ')':
                if mx == 0:
                    return False
                mn = max(mn-1, 0)
                mx -= 1
            elif c == '*':
                mx += 1
                mn = max(mn-1, 0)
            else:
                return False
            # print(mx, mn)
        return mn == 0
