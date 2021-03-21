class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix[0]), len(matrix)

        col0 = False
        row0 = 0 in matrix[0]
        for i in range(n):
            col0 = col0 or not matrix[i][0]
            for j in range(m):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0:
            for i in range(m):
                matrix[0][i] = 0
        if col0:
            for j in range(n):
                matrix[j][0] = 0
                    
