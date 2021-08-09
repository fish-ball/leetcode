class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        acc = [0] + nums
        for i in range(1, n+1):
            acc[i] += acc[i-1]
        ans = 0
        for i, x in enumerate(acc):
            j = bisect.bisect_left(acc, x+goal, i+1)
            k = bisect.bisect_right(acc, x+goal, i+1)
            ans += k - j
        return ans
