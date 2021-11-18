class Solution:
    @lru_cache(None)
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n&1:
            return min(self.integerReplacement(n-1), self.integerReplacement(n+1)) + 1
        return self.integerReplacement(n>>1) + 1
