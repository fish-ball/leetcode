class Solution:
    def maxProduct(self, words: List[str]) -> int:
        h = {}
        for w in words:
            key = reduce(lambda x,y:x|y, (1<<(ord(c)-ord('a')) for c in w), 0)
            h[key] = max(h.get(key, 0), len(w))
        ans = 0
        k = list(h.keys())
        for i, x in enumerate(k):
            for j, y in enumerate(k[:i]):
                if x & y == 0:
                    ans = max(ans, h[x]*h[y])
        return ans
