class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        acc = [0]
        for c in piles:
            acc.append(acc[-1] + c)
        dp = [[0] * n for i in range(n)] # 记录最优残差
        for i in range(n):
            dp[i][i] = -piles[i]
        for k in range(1, n):
            for i in range(n-k):
                j = i + k
                if k & 1: # 轮到甲
                    dp[i][j] = max(piles[i] + dp[i+1][j], dp[i][j-1] + piles[j])
                else: # 轮到乙
                    dp[i][j] = min(-piles[i] + dp[i+1][j], dp[i][j-1] - piles[j])
            # for row in dp:
            #     print(row)
            # print()
        return dp[0][n-1] > 0
