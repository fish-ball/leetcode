class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x+1
        while l < r-1:
            m = l + r >> 1
            if m * m <= x:
                l = m
            else:
                r = m
        return l
