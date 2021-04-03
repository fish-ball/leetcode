class Solution:
    RULES = dict((
        ('M', 1000),
        ('D', 500),
        ('C', 100),
        ('L', 50),
        ('X', 10),
        ('V', 5),
        ('I', 1),
    ))

    def romanToInt(self, s: str) -> int:
        ans = 0
        last = ''
        for c in s:
            if last == 'I' and c == 'V':
                ans += 3
            elif last == 'I' and c == 'X':
                ans += 8
            elif last == 'X' and c == 'L':
                ans += 30
            elif last == 'X' and c == 'C':
                ans += 80
            elif last == 'C' and c == 'D':
                ans += 300
            elif last == 'C' and c == 'M':
                ans += 800
            else:
                ans += Solution.RULES[c]
            last = c
        return ans
