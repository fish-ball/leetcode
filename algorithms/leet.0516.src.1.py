class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for j in range(n):
            for i in range(j-1,-1,-1):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                # [print(x) for x in dp]; print()
        return dp[0][n-1]
