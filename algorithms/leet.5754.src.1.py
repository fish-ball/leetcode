class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n-1):
            if len(set(s[i:i+3])) == 3:
                ans += 1
        return ans
