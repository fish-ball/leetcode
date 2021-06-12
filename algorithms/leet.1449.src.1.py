class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        n = len(cost)
        dp = [-1] * (target+1)
        dp[0] = 0
        for i, c in enumerate(cost):
            for j in range(0, target+1-c):
                # print(f'j={j}')
                if dp[j] > -1:
                    x = int(f'{i+1}{"" if dp[j] == 0 else dp[j] }')
                    # print(x)
                    if dp[j+c] == -1 or dp[j+c] < x:
                        dp[j+c] = x
            # print(dp)
        return str(dp[target]) if dp[target] > -1 else '0'
