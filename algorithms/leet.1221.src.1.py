class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        k = 0
        for x in s:
            k += 1 if x == 'R' else -1
            ans += 0 if k else 1
        return ans
