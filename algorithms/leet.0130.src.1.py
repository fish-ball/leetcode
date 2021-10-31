class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        b = board
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(x, y):
            b[x][y] = 'I'
            for dx, dy in d:
                xx = x + dx
                yy = y + dy
                if 0<=xx<m and 0<=yy<n and b[xx][yy] == 'O':
                    dfs(xx, yy)
        for i in range(m):
            if b[i][0] == 'O':
                dfs(i, 0)
            if b[i][n-1] == 'O':
                dfs(i, n-1)
        for j in range(1, n-1):
            if b[0][j] == 'O':
                dfs(0, j)
            if b[m-1][j] == 'O':
                dfs(m-1, j)
        for i in range(m):
            for j in range(n):
                if b[i][j] == 'O':
                    b[i][j] = 'X'
                elif b[i][j] == 'I':
                    b[i][j] = 'O'
        return board
