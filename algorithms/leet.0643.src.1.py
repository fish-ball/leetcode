class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        acc = 0
        ans = -99999999999
        for i, x in enumerate(nums):
            if i >= k:
                acc -= nums[i-k]
            acc += x
            if i >= k-1:
                ans = max(ans, acc)
        return ans / k
                
