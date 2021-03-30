class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = m * n
        while l < r - 1:
            x = l + r >> 1
            if matrix[x // m][x % m] <= target:
                l = x
            else:
                r = x
        return matrix[l // m][l % m] == target
