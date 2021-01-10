class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        p = [-1] * n
        def up(i):
            if p[i] == -1:
                return i
            p[i] = up(p[i])
            return p[i]
        for i, j in pairs:
            i = up(i)
            j = up(j)
            if i != j:
                p[i] = j
            # print(p)
        d = dict()
        for i in range(n):
            k = up(i)
            if k not in d:
                d[k] = set()
            d[k].add(i)
        # print(d)
        sl = list(s)
        for w in d.values():
            l = sorted([s[i] for i in w])
            # print(w, l)
            for i, x in zip(sorted(w), l):
                sl[i] = x
        return ''.join(sl)

