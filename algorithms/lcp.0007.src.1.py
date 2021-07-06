class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        dp = [1] + [0] * (n-1)
        for i in range(k):
            dp2 = [0] * n
            for v, w in relation:
                dp2[w] += dp[v]
            dp = dp2
            # print(dp)
        return dp[n-1]
