class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        i = 0
        while i+k+1 < n:
            if nums[i+k] == nums[i+k+1]:
                k += 1
            else:
                i += 2
        if n-k & 1:
            k += 1
        return k
