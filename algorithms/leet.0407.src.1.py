class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        dp = [[-1] * n for i in range(m)]
        q = []
        for i in range(m):
            dp[i][0] = heightMap[i][0]
            dp[i][n-1] = heightMap[i][n-1]
            heapq.heappush(q, (dp[i][0], i, 0))
            heapq.heappush(q, (dp[i][n-1], i, n-1))
        for j in range(1, n-1):
            dp[0][j] = heightMap[0][j]
            dp[m-1][j] = heightMap[m-1][j]
            heapq.heappush(q, (dp[0][j], 0, j))
            heapq.heappush(q, (dp[m-1][j], m-1, j))
        d = [(0,1), (1,0), (0,-1), (-1,0)]
        while q:
            h, i, j = heappop(q)
            for di, dj in d:
                ii = i + di
                jj = j + dj
                if 0<ii<m-1 and 0<jj<n-1 and \
                        heightMap[ii][jj] <= h and \
                        (dp[ii][jj]==-1 or h < dp[ii][jj]):
                    dp[ii][jj] = h
                    heapq.heappush(q, (h, ii, jj))
                if 0<ii<m-1 and 0<jj<n-1 and \
                        heightMap[ii][jj] > h and \
                        (dp[ii][jj]==-1 or heightMap[ii][jj] < dp[ii][jj]):
                    dp[ii][jj] = heightMap[i][j]
                    heapq.heappush(q, (heightMap[ii][jj], ii, jj))
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += max(0, dp[i][j] - heightMap[i][j])
        return ans


