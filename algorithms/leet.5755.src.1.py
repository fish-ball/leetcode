class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        print(nums[:n//2], nums[n-1:n//2:-1])
        return max([x+y for x, y in zip(nums[:n//2], nums[n-1:n//2-1:-1])])
