class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        nums.append(0)


    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j] - self.nums[i-1]



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
