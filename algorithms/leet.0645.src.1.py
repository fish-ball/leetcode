class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums) - Counter(range(1, len(nums) + 1))
        d = Counter(range(1, len(nums) + 1)) - Counter(nums)
        return list(c.keys()) + list(d.keys())
