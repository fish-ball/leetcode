class Solution:
    def maxLength(self, arr: List[str]) -> int:
        d = {0}
        ans = 0
        for s in arr:
            if len(set(s)) < len(s):
                continue
            m = 0
            for c in s:
                m += 1 << (ord(c)-ord('a'))
            dd = d.copy()
            for k in d:
                if m & k == 0:
                    dd.add(m|k)
                    ans = max(ans, bin(m|k).count('1'))
            d = dd
        return ans
