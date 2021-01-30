class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        mx = 0
        x = 0
        for i, c in enumerate(s):
            if c in last:
                pos = last[c] + 1
                for j in range(x, pos):
                    del last[s[j]]
                x = pos
            last[c] = i
            mx = max(mx, i-x+1)
        return mx
