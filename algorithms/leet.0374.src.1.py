# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = -1
        r = n + 1
        while l + 1 < r:
            m = l + r >> 1
            # print(l, m, r)
            judge = guess(m)
            if judge < 0:
                r = m
            elif judge > 0:
                l = m
            else:
                return m
        return -1
