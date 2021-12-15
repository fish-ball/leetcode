class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [set() for i in range(n)]
        for w, v in richer:
            g[v].add(w)
        @lru_cache(None)
        def dfs(v):
            x = (quiet[v], v)
            for w in g[v]:
                x = min(x, dfs(w))
            return x
        return [dfs(v)[1] for v in range(n)]
