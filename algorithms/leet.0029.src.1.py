class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor
        ans = 0
        p = -1
        while (divisor << p + 1) <= dividend:
            p += 1
        while p >= 0:
            if (divisor << p) <= dividend:
                ans += 1 << p
                dividend -= divisor << p
            p -= 1
        if sign < 0:
            ans = -ans
        if ans < -(1<<31):
            ans = -(1<<31)
        elif ans > (1<<31)-1:
            ans = (1<<31)-1
        return ans
