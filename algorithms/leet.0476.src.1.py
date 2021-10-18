class Solution:
    def findComplement(self, num: int) -> int:
        ans = 0
        p = 0
        while num:
            ans += ((num&1) ^ 1) << p
            # print(bin(ans), bin(num))
            p += 1
            num >>= 1
        return ans
