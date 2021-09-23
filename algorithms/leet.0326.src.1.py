class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return not((3**20) % n) if n > 0 else False
