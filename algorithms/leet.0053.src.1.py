class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = max(nums)
        acc = None
        for x in nums:
            if x < 0:
                if acc and acc + x > 0:
                    acc += x
                else:
                    acc = None
            else:
                acc = max((acc or 0) + x, x)
            if acc is not None:
                ans = max(ans, acc)
        return ans
