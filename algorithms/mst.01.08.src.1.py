class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        r0 = 0 in matrix[0]
        c0 = any([not r[0] for r in matrix])
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if c0:
            for i in range(m):
                matrix[i][0] = 0
        if r0:
            for j in range(n):
                matrix[0][j] = 0
