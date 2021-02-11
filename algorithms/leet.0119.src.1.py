class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [1]
        for i in range(rowIndex):
            a.append(0)
            for i in range(len(a)-1, 0, -1):
                a[i] += a[i-1]
        return a
