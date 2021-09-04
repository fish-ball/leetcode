class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0
        for i, x in enumerate(nums):
            for j in range(i + 1, min(i + x + 1, n)):
                if dp[j] == -1 or dp[j] > dp[i] + 1:
                    dp[j] = dp[i] + 1
        return dp[n-1]
