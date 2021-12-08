class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        acc = [0] * (n+1)
        for i, x in enumerate(nums):
            acc[i+1] = acc[i] + x
        dp = [[(0, -1)] * (n+1) for i in range(3)]
        for i in range(k, n + 1):
            x = acc[i] - acc[i-k]
            # 0 
            if x <= dp[0][i-1][0]:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = (x, i-k)
            # 1
            if not dp[0][i-k][0] or x + dp[0][i-k][0] <= dp[1][i-1][0]:
                dp[1][i] = dp[1][i-1]
            else:
                dp[1][i] = (x+dp[0][i-k][0], i-k)
            # 2            
            if not dp[1][i-k][0] or x + dp[1][i-k][0] <= dp[2][i-1][0]:
                dp[2][i] = dp[2][i-1]
            else:
                dp[2][i] = (x+dp[1][i-k][0], i-k)
            # for row in dp:
            #     print(*[f'{x[0]:-3d}' for x in row])
            # print()
            # for row in dp:
            #     print(*[f'{x[1]:-3d}' for x in row])
            # print('----')
        i = n
        ans = []
        for j in range(2,-1,-1):
            ans.insert(0, dp[j][i][-1])
            i = dp[j][i][-1]
        return ans
