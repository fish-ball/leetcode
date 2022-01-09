class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        s = set(range(1,n+1))
        for row in matrix:
            if s - set(row):
                return False
        for col in zip(*matrix):
            if s - set(col):
                return False
        return True
