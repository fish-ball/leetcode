class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pp = []
        for v, row in enumerate(preferences):
            pp.append([-1] * n)
            for p, w in enumerate(row):
                pp[v][w] = p
        ans = set()
        for i, (xx, yy) in enumerate(pairs):
            for j in range(i):
                uu, vv = pairs[j]
                for x, y, u, v in ((xx, yy, uu, vv),
                                   (xx, yy, vv, uu),
                                   (yy, xx, uu, vv),
                                   (yy, xx, vv, uu),
                                   (uu, vv, xx, yy),
                                   (uu, vv, yy, xx),
                                   (vv, uu, xx, yy),
                                   (vv, uu, yy, xx)):
                    if pp[x][u] < pp[x][y] and pp[u][x] < pp[u][v]:
                        ans.add(x)
        # print(ans)
        return len(ans)
            
