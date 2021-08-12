class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 2:
            return n
        def solve(k):  # 0-9999(k个9)的结果
            if k < 2:
                return k
            return 10 * solve(k-1) + 10**(k-1)
        m = 0
        while 10**(m+1) <= n:
            m += 1
        p = 10 ** m
        ans = solve(m) * (n//p)
        if n // p > 1:
            ans += p
        if n // p == 1:
            ans += n % p + 1
        ans += self.countDigitOne(n%p)
        return ans
