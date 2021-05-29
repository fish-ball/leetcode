class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        a = 0
        ma = 0
        b = 0
        mb = 0
        last = ''
        for c in s:
            if c == '1':
                if last == c:
                    a += 1
                else:
                    a = 1
                ma = max(ma, a)
            else:
                if last == c:
                    b += 1
                else:
                    b = 1
                mb = max(mb, b)
            last = c
        return ma > mb
