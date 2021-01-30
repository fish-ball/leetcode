class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        g = [-1] * (m*n)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        hq = [(grid[0][0], (0, 0))]

        while hq:
            v, (x, y) = heappop(hq)
            # print(f'bfs({x}, {y}) = {v}')
            if -1 != g[x*m+y] <= v:
                continue
            g[x*m+y] = v
            for xx, yy in zip(dx, dy):
                x0 = x + xx
                y0 = y + yy
                if not (0 <= x0 < n and 0 <= y0 < m):
                    continue
                vv = max(v, grid[x0][y0])
                if g[x0*m+y0] == -1 or g[x0*m+y0] > vv:
                    heappush(hq, (vv, (x0, y0)))

        return g[-1]
