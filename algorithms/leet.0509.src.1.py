class Solution:
    def fib(self, n: int) -> int:
        a = [0, 1]
        while len(a) < 31:
            a.append(a[-1] + a[-2])
        return a[n]
