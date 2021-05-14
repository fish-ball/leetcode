from sortedcontainers import SortedSet

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        g = [[0]*(m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                g[i+1][j+1] = g[i][j+1] + g[i+1][j] - g[i][j] + matrix[i][j]
        ans = None
        for i1 in range(n+1):
            for i2 in range(i1):
                s = SortedSet([0])
                for j in range(1, m+1):
                    acc = g[i1][j] - g[i2][j]
                    p = s.bisect_left(acc - k)
                    # print(s, acc, 'find:', acc-k, '=', p)
                    if p < len(s) and acc - s[p] <= k and (ans is None or acc - s[p] > ans):
                        ans = acc - s[p]
                    s.add(acc)
        return ans


