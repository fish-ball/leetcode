class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max([a+b for a,b in zip(nums, nums[::-1])])
