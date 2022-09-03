class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        arr = []
        b = [[-1] * m for i in range(n)]
        b[start[0]][start[1]] = 0
        q = Deque([(0, start)])
        d = ((0,1), (1,0), (0,-1), (-1,0))
        while q:
            h, (x, y) = q.popleft()
            for dx, dy in d:
                xx = x + dx
                yy = y + dy
                if 0<=xx<n and 0<=yy<m and grid[xx][yy] and b[xx][yy] == -1:
                    b[xx][yy] = h + 1
                    q.append((h+1, (xx, yy)))
        for i, row in enumerate(grid):
            for j, p in enumerate(row):
                if not pricing[0] <= p <= pricing[1]:
                    continue
                if b[i][j] == -1:
                    continue
                arr.append([b[i][j],p,[i,j]])
        arr.sort()
        return [x[-1] for x in arr[:k]]
