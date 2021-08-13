class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs)
        mp = {}
        g = {}
        for x, y in adjacentPairs:
            mp[x] = mp.get(x, 0) + 1
            mp[y] = mp.get(y, 0) + 1
            if x not in g:
                g[x] = {}
            if y not in g:
                g[y] = {}
            g[x][y] = g[x].get(y, 0) + 1
            g[y][x] = g[y].get(x, 0) + 1
        for x, k in mp.items():
            if k % 2 == 1:
                break
        ans = []
        while True:
            ans.append(x)
            if not g[x]:
                break
            y = next(iter(g[x].keys()))
            # print(x, y)
            g[x][y] -= 1
            g[y][x] -= 1
            if not g[x][y]:
                del g[x][y]
            if not g[y][x]:
                del g[y][x]
            # for a, b in g.items():
            #     print(a, b)
            x = y
        return ans


            


