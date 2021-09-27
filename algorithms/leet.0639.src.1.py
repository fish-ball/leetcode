class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 1000000007
        dp = [0, 0, 0, 0, 0, 0, 0, 0, 1, # 0-9
              0, 0, 0] # 10-12
        for c in s:
            ss = sum(dp)
            dp2 = [0] * 13
            if c == '0':
                dp2[0] = (dp2[0] + dp[1] + dp[2]) % MOD
            for k in range(1, 10):
                if c == '*' or c == str(k):
                    dp2[k] = (dp2[k] + ss) % MOD
            if c == '1' or c == '*':
                dp2[11] = (dp2[11] + dp[1] + dp[2]) % MOD
            if c == '2' or c == '*':
                dp2[12] = (dp2[12] + dp[1] + dp[2]) % MOD
            for k in range(3, 7):
                if c == '*' or c == str(k):
                    dp2[k] = (dp2[k] + dp[1] + dp[2]) % MOD
            for k in range(7, 10):
                if c == '*' or c == str(k):
                    dp2[k] = (dp2[k] + dp[1]) % MOD
            dp = dp2
            # print(dp)
        return sum(dp) % MOD
