class Solution:
    # @return an integer
    def reverse(self, x):
        return -self.reverse(-x) if x < 0 else 0 if int(str(x)[::-1]) > 2**31 else int(str(x)[::-1])
