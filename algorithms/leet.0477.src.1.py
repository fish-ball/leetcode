class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(31):
            k = sum([1 for x in nums if x & (1<<i)])
            ans += (n-k) * k
        return ans
