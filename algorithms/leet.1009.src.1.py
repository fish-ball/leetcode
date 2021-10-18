class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if not n: return 1
        ans = 0
        p = 0
        while n:
            ans += ((n&1) ^ 1) << p
            # print(bin(ans), bin(n))
            p += 1
            n >>= 1
        return ans
