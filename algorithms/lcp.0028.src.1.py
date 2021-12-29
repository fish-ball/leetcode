class Solution:
    def purchasePlans(self, nums: List[int], target: int) -> int:
        ans = 0
        m = 1000000007
        nums.sort()
        for i, x in enumerate(nums):
            j = bisect.bisect_right(nums, target-x)
            ans += max(0,j-i-1)
            ans %= m
        return ans
