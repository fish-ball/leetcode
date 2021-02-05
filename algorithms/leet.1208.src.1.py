class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        a = [abs(ord(x)-ord(y)) for x, y in zip(s, t)]
        j = 0
        ans = 0
        acc = 0
        for i in range(n):
            while j < i:
                acc += a[j]
                j += 1
            while j < n and a[j] + acc <= maxCost:
                acc += a[j]
                j += 1
                ans = max(ans, j - i)
            acc -= a[i]
        return ans

