class Solution:
    def trap(self, height: List[int]) -> int:
        a = []
        b = []
        for x, y in zip(height, height[::-1]):
            a.append(max(a[-1], x) if a else x)
            b.append(max(b[-1], y) if b else y)
        ans = 0
        for a, x, y in zip(height, a, b[::-1]):
            ans += min(x, y) - a
        return ans
