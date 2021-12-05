class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        j = 0
        for i in range(k):
            nums[j] = -nums[j]
            if j+1 < len(nums) and nums[j+1] < nums[j]:
                j += 1
        return sum(nums)
