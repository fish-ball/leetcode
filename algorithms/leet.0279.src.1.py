class Solution:
    def numSquares(self, n: int) -> int:
        dp = list(range(n+1))
        i = 1
        while i * i <= n:
            for j in range(0, n+1-i*i):
                dp[j+i*i] = min(dp[j+i*i], dp[j]+1)
            i += 1
        return dp[n]
