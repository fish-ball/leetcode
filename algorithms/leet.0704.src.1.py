class Solution:
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        return idx if nums[idx] == target else -1
