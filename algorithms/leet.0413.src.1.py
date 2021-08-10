class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        last = None
        k = 0
        ans = 0
        for i in range(1, n):
            x = nums[i] - nums[i-1]
            if last != x:
                ans  += k * (k - 1) // 2
                last = x
                k = 1
            else:
                k += 1
        ans += k * (k - 1) // 2
        return ans
