class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(100):
            m = 0
            while n:
                m += (n%10)**2
                n //= 10
            n = m
            if n == 1:
                return True
        return False
