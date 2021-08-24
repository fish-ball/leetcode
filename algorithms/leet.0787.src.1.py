class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = {}
        for u, v, p in flights:
            if u not in g:
                g[u] = {}
            g[u][v] = p
        dp = {src: 0}
        for i in range(k+1):
            dp2 = dict(dp)
            for u, w in dp.items():
                for v, p in g.get(u, {}).items():
                    ww = w + p
                    if v not in dp2:
                        dp2[v] = ww
                    else:
                        dp2[v] = min(dp2[v], ww)
            # print(dp2)
            dp = dp2
        return dp.get(dst, -1)
