class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        i = 0
        j = 0
        di = -1
        dj = 1
        ans = []
        for k in range(m * n):
            print(di, dj, i, j)
            ans.append(mat[i][j])
            if 0 <= i + di < m and 0 <= j + dj < n:
                i += di
                j += dj
            elif di < 0 and j == n-1 or di > 0 and i < m-1:
                i += 1
                di = -di
                dj = -dj
            else:
                j += 1
                di = -di
                dj = -dj
        return ans
