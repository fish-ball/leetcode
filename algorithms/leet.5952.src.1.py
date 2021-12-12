class Solution:
    def countPoints(self, rings: str) -> int:
        d = {}
        bm = {'B': 1, 'R': 2, 'G':4}
        for c, i in zip(rings[::2], rings[1::2]):
            if i not in d:
                d[i] = 0
            d[i] |= bm[c]
        return sum(1 for x in d.values() if x == 7)
