class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = dict()
        g = dict()
        for (a, b), v in zip(equations, values):
            g[a] = g.get(a, [])
            g[b] = g.get(b, [])
            g[a].append((b, v))
            g[b].append((a, 1.0/v))
        p = 0
        def dfs(a, x):
            d[a] = (x, p)
            for b, v in g.get(a, []):
                if b not in d:
                    dfs(b, x / v)
        for c in g:
            if c not in d:
                dfs(c, 1.0)
                p += 1
        result = []
        for a, b in queries:
            if a in d and b in d and d[a][1] == d[b][1]:
                result.append(d[a][0] / d[b][0])
            else:
                result.append(-1.0)
        return result
                
