class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            mx = nums[i]
            for j in range(i-1):
                mx = max(mx, nums[i] + dp[j])
            dp[i] = mx
        return max(dp)
