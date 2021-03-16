class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        i = 0
        j = 0
        for k in range(min(m, n)):
            ans.append(matrix[i][j])
            if k % 2:
                for p in range(m-1):
                    j -= 1
                    ans.append(matrix[i][j])
                for p in range(n-1):
                    i -= 1
                    ans.append(matrix[i][j])
                j += 1
            else:
                for p in range(m-1):
                    j += 1
                    ans.append(matrix[i][j])
                for p in range(n-1):
                    i += 1
                    ans.append(matrix[i][j])
                j -= 1
            m -= 1
            n -= 1
        return ans
