class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(None)
        def calc(l, r):
            if l >= r:
                return 0
            return min((max(calc(l,m-1),calc(m+1,r))+m for m in range(l,r+1)))
        return calc(1, n)
