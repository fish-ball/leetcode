class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        g = [set() for i in range(n)]
        d = [0] * n
        for v, e in enumerate(graph):
            for w in e:
                g[w].add(v)
                d[v] += 1
        ans = []
        q = [v for v, x in enumerate(d) if x == 0]
        while q:
            w = q.pop()
            ans.append(w)
            for v in g[w]:
                d[v] -= 1
                if d[v] == 0:
                    q.append(v)
        return sorted(ans)
