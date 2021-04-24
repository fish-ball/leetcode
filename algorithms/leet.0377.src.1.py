class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for v in range(1, target+1):
            for x in nums:
                if 0 <= v-x < target:
                    dp[v] += dp[v-x]
        return dp[target]
