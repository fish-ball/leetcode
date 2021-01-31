class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        p = list(range(n))
        m = n
        def find(k):
            if p[k] == k:
                return k
            p[k] = find(p[k])
            return p[k]
        for i in range(n):
            for j in range(i+1, n):
                v = find(i)
                w = find(j)
                if v == w:
                    continue
                if sum(int(x!=y) for x, y in zip(strs[i], strs[j])) in (0,2):
                    p[v] = w
                    m -= 1
        return m
        
