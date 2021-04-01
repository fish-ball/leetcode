class Solution:
    def clumsy(self, N: int) -> int:
        ans = 0
        while N > 0:
            vals = list(range(N, max(N-4, 0), -1))
            x = vals[0]
            if len(vals) > 1:
                x *= vals[1]
            if len(vals) > 2:
                x //= vals[2]
            ans = ans - x if ans else x
            if len(vals) > 3:
                ans += vals[3]
            N -= 4
        return ans
