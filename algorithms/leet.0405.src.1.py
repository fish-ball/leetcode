class Solution:
    def toHex(self, num: int) -> str:
        ans = ''
        for i in range(8):
            ans += '0123456789abcdef'[num&15]
            num >>= 4
            if not num:
                break
        return ans[::-1]
