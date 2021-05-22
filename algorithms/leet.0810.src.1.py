class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        n = len(nums)
        acc = reduce(lambda x, y: x ^ y, nums)
        if not acc:
            return True
        return n % 2 == 0
