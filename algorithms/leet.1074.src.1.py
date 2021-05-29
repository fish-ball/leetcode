class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        g = [[0]*(m+1) for i in range(n+1)]
        for i in range(n):
            for j in range(m):
                g[i+1][j+1] = matrix[i][j] + g[i][j+1] + g[i+1][j] - g[i][j]
        ans = 0
        # [print(row) for row in g]; print('----')
        for i2 in range(n+1):
            for i1 in range(i2):
                dd = {0: 1}
                for j2 in range(1, m+1):
                    expect = g[i2][j2] - g[i1][j2] - target
                    # print(f'i = [{i1}-{i2}], j = [?-{j2}]', expect, dd)
                    ans += dd.get(expect, 0)
                    val = g[i2][j2] - g[i1][j2]
                    dd[val] = dd.get(val, 0) + 1
        return ans

        

