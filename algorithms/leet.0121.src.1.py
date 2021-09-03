class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        k = prices[0]
        for x in prices:
            if x < k:
                k = x
            else:
                ans = max(ans, x - k)
        return ans
