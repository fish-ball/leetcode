class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y, range(len(nums)+1), 0) ^ reduce(lambda x,y:x^y, nums, 0)
