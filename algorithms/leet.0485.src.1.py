class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        acc = 0
        for x in nums:
            if x:
                acc += 1
                ans = max(ans, acc)
            else:
                acc = 0
        return ans
