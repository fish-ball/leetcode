class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return not (n & n-1) and n % 3 == 1
