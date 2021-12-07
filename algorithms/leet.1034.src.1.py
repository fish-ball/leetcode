class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        c = grid[row][col]
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        def dfs(x, y):
            grid[x][y] = -c
            for xx, yy in zip(dx, dy):
                xx += x
                yy += y
                if 0<=xx<m and 0<=yy<n and grid[xx][yy] >= 0 and grid[xx][yy]==c:
                    dfs(xx, yy)
        dfs(row, col)
        s = set()
        for x in range(m):
            for y in range(n):
                if grid[x][y] != -c:
                    continue
                for xx, yy in zip(dx, dy):
                    xx += x
                    yy += y
                    if xx<0 or xx>=m or yy<0 or yy>=n or grid[xx][yy]!=-c:
                        s.add((x,y))
                        break
        # print(grid, s)
        for x,y  in s:
            grid[x][y] = color
        for x in range(m):
            for y in range(n):
                if grid[x][y] < 0:
                    grid[x][y] = c
        return grid
            
