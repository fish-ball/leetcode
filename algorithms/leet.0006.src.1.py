class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = s[0::numRows*2-2]
        for i in range(1, numRows-1):
            for x, y in zip(s[i::numRows*2-2], s[numRows*2-2-i::numRows*2-2]+'-'):
                ans += x + ('' if y == '-' else y)
        ans += s[numRows-1::numRows*2-2]
        return ans
