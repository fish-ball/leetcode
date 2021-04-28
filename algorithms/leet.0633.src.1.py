class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        d = set()
        for i in range(1<<16):
            d.add(i * i)
        for i in range(c + 1):
            if i * i > c:
                break
            if c - i * i in d:
                return True
        return False
