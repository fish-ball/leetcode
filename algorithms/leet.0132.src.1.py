class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        g = [[False] * n for i in range(n)]
        for i in range(n):
            g[i][i] = True
        for k in range(1, n):
            for i in range(0, n-k):
                g[i][i+k] = s[i] == s[i+k] and (True if k <= 2 else g[i+1][i+k-1])
        # for i in g:
        #     print([int(x) for x in i])
        dp = [-1] * (n+1)
        # pre = [-1] * (n+1)
        dp[0] = 0
        for i in range(n):
            for j in range(i, n):
                if g[i][j] and (dp[j+1] == -1 or dp[j+1] > dp[i] + 1):
                    dp[j+1] = dp[i] + 1
                    # pre[j+1] = i
        # ans = []
        # p = n
        # while p > 0:
        #     q = pre[p]
        #     ans.append(s[q:p])
        #     p = q
        # return ans[::-1]
        return dp[n] - 1
