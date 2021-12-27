class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        n = len(nums)
        k += 1
        for i in range(min(k, n)):
            if nums[i] in s:
                return True
            s.add(nums[i])
        for i in range(k, n):
            s.remove(nums[i-k])
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False
