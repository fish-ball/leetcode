class Solution:
    def findLHS(self, nums: List[int]) -> int:
        c = Counter(nums)
        p = sorted(c.items())
        ans = 0
        for i in range(1, len(c)):
            if p[i][0] == p[i-1][0] + 1:
                ans = max(ans, p[i][1]+p[i-1][1])
        return ans
