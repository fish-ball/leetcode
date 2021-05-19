class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        acc1 = [0] * (n+1)
        acc2 = [0] * (n+1)
        ans = []
        for i in range(m):
            for j in range(n):
                x = acc1[j] ^ acc2[j] ^ acc1[j+1] ^ matrix[i][j]
                acc2[j+1] = x
                ans.append(x)
            acc2, acc1 = acc1, acc2
        ans.sort()
        return ans[-k]
