class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        ans = 0
        g = [[0] * n for i in range(m)]
        g[startRow][startColumn] = 1
        for t in range(maxMove):
            gg = [[0] * n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    if not g[i][j]:
                        continue
                    for dx, dy in [[0,1],[1,0],[0,-1],[-1,0]]:
                        ii = i + dx
                        jj = j + dy
                        if 0 <= ii < m and 0 <= jj < n:
                            gg[ii][jj] += g[i][j]
                            gg[ii][jj] %= 1000000007
                        else:
                            ans += g[i][j]
                            ans %= 1000000007
            g = gg
        return ans


            
