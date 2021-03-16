class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = b = nums[k]
        i = j = k
        while i > 0 or j < n-1:
            while i > 0 and nums[i-1] >= b:
                i -= 1
            while j < n-1 and nums[j+1] >= b:
                j += 1
            ans = max(ans, (j-i+1)*b)
            if i > 0 and (j == n-1 or nums[i-1] > nums[j+1]):
                b = nums[i-1]
            elif j < n-1:
                b = nums[j+1]
        ans = max(ans, b*n)
        return ans
