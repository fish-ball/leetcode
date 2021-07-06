class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n <= 0:
            return 1
        x = self.countGoodNumbers(n // 4 * 2)
        x *= x
        if n % 4 == 1:
            x *= 5
        elif n % 4 == 2:
            x *= 20
        elif n % 4 == 3:
            x *= 100
        x %= 1000000007 
        return x
