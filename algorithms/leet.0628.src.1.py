class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        results = []
        results.append(nums[-1] * nums[-2] * nums[-3])
        results.append(nums[0] * nums[1] * nums[-1])
        return max(results)
