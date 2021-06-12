class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        ans = 0
        while i < n:
            i += 1
            while i < n and nums[i] == nums[i-1]:
                i += 1
            ans += n - i
        return ans
