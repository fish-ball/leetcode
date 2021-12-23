class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        r = {}
        for a, b in zip(s, t):
            if a in d:
                if d[a] != b:
                    return False
            elif b in r:
                return False
            d[a] = b
            r[b] = a
        return True
