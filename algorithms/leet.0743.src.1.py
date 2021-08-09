class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dp = [[-1] * n for i in range(n)]
        for u, v, w in times:
            dp[u-1][v-1] = w if dp[u-1][v-1] == -1 else min(dp[u-1][v-1])
        for p in range(n):
            for i in range(n):
                for j in range(n):
                    if dp[i][p] == -1 or dp[p][j] == -1:
                        continue
                    w = dp[i][p] + dp[p][j]
                    if dp[i][j] == -1 or dp[i][j] > w:
                        dp[i][j] = w
        # for row in dp:
            # print(row)
        dp[k-1][k-1] = 0
        if min(dp[k-1]) == -1:
            return -1
        return max(dp[k-1])
