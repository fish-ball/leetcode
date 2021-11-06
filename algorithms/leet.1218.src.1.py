class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ans = 1
        d = {}
        for x in arr:
            d[x] = max(d.get(x, 1), d.get(x-difference, 0)+1)
            ans = max(ans, d[x])
        return ans
