class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num+1
        while l < r-1:
            m = l + r >> 1
            if m * m > num:
                r = m
            elif m * m < num:
                l = m
            else:
                return True
        return l * l == num
