class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        g = [[0] * (m+1) for i in range(n+1)]
        
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                g[i+1][j+1] = x + g[i+1][j] + g[i][j+1] - g[i][j]
                
        # for row in g:
        #     print(row)
                
        def is_magic(i, j, k):
            # print(f'is_magic({i}, {j}, {k})')
            s = g[i+k][j+k] - g[i][j+k] - g[i+k][j] + g[i][j]
            # print(f's = {s}')
            if s % k > 0:
                return False
            r = s // k
            # print(f'r = {r}')
            for ii in range(i, i+k):
                si = g[ii+1][j+k] - g[ii][j+k] - g[ii+1][j] + g[ii][j]
                # print(ii, si)
                if si != r:
                    return False
            for jj in range(j, j+k):
                sj = g[i+k][jj+1] - g[i][jj+1] - g[i+k][jj] + g[i][jj]
                # print(jj, sj)
                if sj != r:
                    return False
            s1 = 0
            s2 = 0
            for ii in range(k):
                s1 += grid[i+ii][j+ii]
                s2 += grid[i+k-1-ii][j+ii]
            if s1 != r or s2 != r:
                return False
            return True
            
        for k in range(min(n, m), 0, -1):
            for i in range(n+1-k):
                for j in range(m+1-k):
                    if is_magic(i, j, k):
                        return k
        return 1
            
