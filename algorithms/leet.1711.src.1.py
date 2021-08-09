class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        ans = 0
        c = dict(Counter(deliciousness))
        for x, v in sorted(c.items()):
            for m in range(22, -1, -1):
                y = (1<<m) - x
                if y < x:
                    break
                if y == x:
                    ans += v*(v-1)//2
                elif y in c:
                    ans += v*c[y]
                ans %= 1000000007
        return ans
