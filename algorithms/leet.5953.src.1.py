class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            mx = None
            mn = None
            for j in range(i, n):
                mx = nums[j] if mx is None or mx < nums[j] else mx
                mn = nums[j] if mn is None or mn > nums[j] else mn
                ans += mx - mn
        return ans
                
