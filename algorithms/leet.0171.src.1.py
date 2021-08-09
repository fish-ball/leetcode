class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        acc = 1
        x = 0
        for c in columnTitle:
            ans += acc
            acc *= 26
            x *= 26
            x += ord(c) - ord('A')
        return ans + x
