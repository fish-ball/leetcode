class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        if not matrix:
            return
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i > 0:
                    matrix[i][j] += matrix[i-1][j]
                if j > 0:
                    matrix[i][j] += matrix[i][j-1]
                if i > 0 and j > 0:
                    matrix[i][j] -= matrix[i-1][j-1]
        # for r in self.mat: print(r)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.mat:
            return 0
        a = 0 if row1 == 0 or col1 == 0 else self.mat[row1-1][col1-1]
        b = 0 if row1 == 0 else self.mat[row1-1][col2]
        c = 0 if col1 == 0 else self.mat[row2][col1-1]
        # print(a, b, c, self.mat[row2][col2])
        return self.mat[row2][col2] - b - c + a



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
