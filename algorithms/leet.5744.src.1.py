class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        b = list(zip(*box))
        n = len(b)
        for i in range(n):
            b[i] = list(b[i][::-1])
        m = len(b[0])
        for j in range(m):
            k = n - 1
            for i in range(n-1, -1, -1):
                # print(i, j)
                # print(b[i][j])
                # print(k)
                while k > 0 and b[k][j] != '.':
                    k -= 1
                if i > k:
                    continue
                if b[i][j] ==  '*':
                    k = i
                elif b[i][j] == '#':
                    # print(i, k, j)
                    b[k][j], b[i][j] = b[i][j], b[k][j]
                    k -= 1
                elif b[i][j] == '.':
                    continue
        return b
