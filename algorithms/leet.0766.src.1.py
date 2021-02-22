class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(-m+1, n):
            s = set()
            for j in range(m):
                ii = i+j
                if 0 <= ii < n:
                    s.add(matrix[ii][j])
            if len(s) > 1:
                return False
        return True

