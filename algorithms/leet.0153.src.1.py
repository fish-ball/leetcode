class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n
        while l < r - 1:
            m = l + r >> 1
            if nums[l] < nums[m]:
                l = m
            else:
                r = m
        return nums[r % n]
