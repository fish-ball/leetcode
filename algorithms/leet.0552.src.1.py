class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 1000000007
        dp = {(0,0): 1}
        for k in range(n):
            dp2 = dict()
            for (a, l), v in dp.items():
                if a < 1:
                    dp2[(a+1, 0)] = (dp2.get((a+1, 0), 0) + v) % MOD
                if l < 2:
                    dp2[(a, l+1)] = (dp2.get((a, l+1), 0) + v) % MOD
                dp2[(a, 0)] = (dp2.get((a, 0), 0) + v) % MOD
            dp = dp2
            # print([(x, y) for x, y in sorted(dp.items())])
        return sum(dp.values()) % MOD
