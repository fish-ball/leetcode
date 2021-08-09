class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            x = nums[i]
            for j in range(i+1, n):
                y = nums[j]
                ans += bisect.bisect_left(nums, x+y, j+1, n) - j - 1
                
        return ans
