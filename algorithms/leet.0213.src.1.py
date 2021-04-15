class Solution:
    def rob2(self, nums):
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
        
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.rob2(nums[:-1]), self.rob2(nums[1:]))
