class Solution:
    def maxPower(self, s: str) -> int:
        if not s:
            return 0
        ans = 1
        combo = 1
        last = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                combo += 1
            else:
                combo = 1
            ans = max(ans, combo)
        return ans
