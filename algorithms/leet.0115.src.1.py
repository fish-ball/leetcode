class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [0] * (m + 1)
        dp[0] = 1
        for i, c in enumerate(s):
            for j in range(m, 0, -1):
                if t[j-1] != c:
                    continue
                dp[j] += dp[j-1]
            # print(dp)
        return dp[m]
