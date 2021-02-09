from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = dict(Counter(s1))
        k = -1
        rem = len(s1)
        for i, a in enumerate(s2):
            while k < i and c.get(a, 0) <= 0:
                k += 1
                if s2[k] in c:
                    c[s2[k]] += 1
                    rem += 1
            if c.get(a, 0) > 0:
                c[a] -= 1
                rem -= 1
            if not rem:
                return True
        return False
