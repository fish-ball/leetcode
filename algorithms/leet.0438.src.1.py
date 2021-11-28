class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        ss = set()
        d = Counter(p)
        d.subtract(Counter(s[:m]))
        ans = []
        if set(d.values()) == {0}:
            ans.append(0)
        for i in range(m, n):
            j = i - m
            d.subtract(Counter({s[i]: 1}))
            d.subtract(Counter({s[j]: -1}))
            if set(d.values()) == {0}:
                ans.append(i-m+1)
        return ans
