class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        for d in range(n):
            for i in range(0, n-d):
                j = i + d
                if d == 0:
                    dp[i][j] = 1
                    continue
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                    continue
                dp[i][j] = d + 1
                for k in range(d):
                    if dp[i][j] > dp[i][i+k] + dp[i+k+1][j]:
                        dp[i][j] = dp[i][i+k] + dp[i+k+1][j]
        return dp[0][n-1]
