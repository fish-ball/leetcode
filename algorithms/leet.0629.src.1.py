class Solution:
    @lru_cache(None)
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 1000000007
        L = 1001
        a = [1] + [0] * k
        for i in range(1, n+1):
            b = [1] + [0] * k
            for j in range(1, k+1):
                b[j] = (b[j-1] + a[j] - (a[j-i] if j>=i else 0)) % mod
            a = b
            # print(a)
        return a[k]
