class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = n
        ans = [[0] * n for i in range(n)]
        i = 0
        j = 0
        x = 1
        for k in range(min(m, n)):
            ans[i][j] = x
            x += 1
            if k % 2:
                for p in range(m-1):
                    j -= 1
                    ans[i][j] = x
                    x += 1
                for p in range(n-1):
                    i -= 1
                    ans[i][j] = x
                    x += 1
                j += 1
            else:
                for p in range(m-1):
                    j += 1
                    ans[i][j] = x
                    x += 1
                for p in range(n-1):
                    i += 1
                    ans[i][j] = x
                    x += 1
                j -= 1
            m -= 1
            n -= 1
        return ans
