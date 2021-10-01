class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        c = dict()
        for a, b in paths:
            c[a] = c.get(a,0)-1
            c[b] = c.get(b,0)+1
        return [k for k in c if c[k] == 1][0]
