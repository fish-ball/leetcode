class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        m = 0
        for i, x in enumerate(nums):
            if x != val:
                nums[m] = x
                m += 1
        return m
