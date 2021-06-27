class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp1 = [0]
        dp2 = [0]
        for x in nums:
            a = max(dp1[-1], dp2[-1] + x)
            b = max(dp2[-1], dp1[-1] - x)
            dp1.append(a)
            dp2.append(b)
        # print(dp1)
        # print(dp2)
        return max(dp2[-1], dp1[-1])
