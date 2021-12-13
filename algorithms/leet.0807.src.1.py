class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dd = [(0,1), (1,0), (0,-1), (-1,0)]
        @lru_cache(None)
        def dfs(i, j, d):
            ii = i + dd[d][0]
            jj = j + dd[d][1]
            if ii<0 or ii>=n or jj<0 or jj>=m:
                return grid[i][j]
            return max(grid[i][j], dfs(ii, jj, d))
        ans = 0
        for i in range(n):
            for j in range(m):
                # print(dfs(i, j, 1), end=' ')
                # print(min([dfs(i, j, d) for d in range(4)]), end=' ')
                ans += min(max(dfs(i,j,0),dfs(i,j,2)), max(dfs(i,j,1),dfs(i,j,3))) - grid[i][j]
            # print()
        return ans
