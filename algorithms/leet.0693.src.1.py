class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n <= 2:
            return True
        if n & 3 in (3, 0):
            return False
        return self.hasAlternatingBits(n>>1)
