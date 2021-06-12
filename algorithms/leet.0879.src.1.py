class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        m = len(group)
        # dp[n][p] 代表用了 n 个人，达到 p 利润的选择数
        dp = [[0] * (minProfit+1) for i in range(n+1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(n-g, -1, -1):
                for j in range(minProfit, -1, -1):
                    ii = i + g
                    jj = min(j+p, minProfit)
                    dp[ii][jj] += dp[i][j]
                    dp[ii][jj] %= 1000000007
            # print(f'g={g}, p={p}')
            # for row in dp:
            #     print(row)
        return sum(
            dp[i][minProfit]
            for i in range(0, n+1)
        ) % 1000000007
