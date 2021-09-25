class Solution:
    def getSum(self, a: int, b: int) -> int:
        m = (1<<11)-1
        while b:
            # print(bin(a), bin(b))
            a, b = (a^b)&m, ((a&b)<<1)&m
        return a if a < 1024 else ~(m^a)
