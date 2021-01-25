class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        def idx(t, x, y):
            return ((t*(n+1)+x)*(n+1)+y)

        n = len(grid)
        g = [0] * ((n+1)*(n+1)*2)
        
        def dfs(t, x, y, d=0):
            if g[idx(t, x, y)]:
                # print(f'   {t}, {x}, {y}')
                return 0
                
            # print('  '*d,d,f'dfs({t}, {x}, {y})')
            g[idx(t, x, y)] = 1
            if t == 0: # 横向
                # 上格
                if x > 0:
                    c = grid[x-1][y]
                    # print(f'  c1 {c}')
                    if c in r' /' and y < n:
                        dfs(1, x-1, y+1, d+1)
                    if c in r' \\':
                        dfs(1, x-1, y, d+1)
                    if c == ' ':
                        dfs(0, x-1, y, d+1)
                # 下格
                if x < n:
                    c = grid[x][y]
                    # print(f'  c2 {c}')
                    if c in r' /':
                        dfs(1, x, y, d+1)
                    if c in r' \\' and y < n:
                        dfs(1, x, y+1, d+1)
                    if c == r' ':
                        dfs(0, x+1, y, d+1)
            else: # 纵向
                # 左格
                if y > 0:
                    c = grid[x][y-1]
                    # print(f'  c3 {c}')
                    if c in r' /' and x < n:
                        dfs(0, x+1, y-1, d+1)
                    if c in r' \\':
                        dfs(0, x, y-1, d+1)
                    if c == r' ':
                        dfs(1, x, y-1, d+1)
                # 右格
                if y < n:
                    c = grid[x][y]
                    # print(f'  c4 {c}')
                    if c in r' /':
                        dfs(0, x, y, d+1)
                    if c in r' \\' and x < n:
                        dfs(0, x+1, y, d+1)
                    if c == r' ':
                        dfs(1, x, y+1, d+1)
            # print('  '*d, '<< 1')
            return 1

        ans = 0
        for i in range(n):
            for j in range(n+1):
                ans += dfs(1, i, j)
                ans += dfs(0, j, i)

        return ans
