class Solution:

    def __init__(self, nums: List[int]):
        self.buf = nums[:]
        self.nums = nums

    def reset(self) -> List[int]:
        self.nums[:] = self.buf[:]
        return self.nums

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
