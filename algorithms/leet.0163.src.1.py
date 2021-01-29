from heapq import heappush, heappop

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        g = [-1] * (m*n)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        hq = [(0, (0, 0))]

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
                vv = max(v, abs(heights[x0][y0]-heights[x][y]))
                if g[x0*m+y0] == -1 or g[x0*m+y0] > vv:
                    heappush(hq, (vv, (x0, y0)))

        return g[-1]
