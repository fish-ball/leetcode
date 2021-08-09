class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        acc = 0
        ans = max(nums)
        if ans < 0:
            return ans
        for x in nums:
            if acc + x >= 0:
                acc += x
                ans = max(ans, acc)
            else:
                acc = 0
        return ans
