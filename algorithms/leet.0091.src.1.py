class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0
        a = 1
        b = 1
        for i in range(1, len(s)): 
            c = s[i-1]
            d = s[i]
            e = 0
            if d == '0':
                if c not in '12':
                    return 0
                e += a
            elif c == '1':
                e += a + b
            elif c == '2':
                if d <= '6':
                    e += a + b
                else:
                    e += b
            else:
                e += b
            a, b = b, e
        return b
