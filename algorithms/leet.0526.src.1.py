class Solution:
    def countArrangement(self, n: int) -> int:
        dp = [0] * (1<<n)
        dp[0] = 1
        for k in range(n): # 第i个数字
            dp2 = [0] * (1<<n)
            # print(f'k = {k}')
            for mask in range((1<<n)):
                if not dp[mask]:
                    continue
                for i in range(n):
                    ii = 1<<i
                    if (ii&mask) or (i+1)%(k+1) and (k+1)%(i+1):
                        continue
                    dp2[mask|ii] += dp[mask]
                    # print(bin(mask)[2:], dp2[mask])
            dp = dp2
        return dp[(1<<n)-1]

