class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnNumber -= 1
        level = 1
        while columnNumber >= 26 ** level:
            columnNumber -= 26 ** level
            level += 1
        return ''.join([chr(ord('A') + columnNumber // 26**i % 26) for i in range(level)])[::-1]
