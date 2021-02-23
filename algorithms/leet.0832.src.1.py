class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            row.reverse()
            for i, x in enumerate(row):
                row[i] = 1 - x
        return A
