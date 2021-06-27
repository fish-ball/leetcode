class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        d = {1: 0}
        q = deque([1])
        def location(k):
            k -= 1
            i = k // n
            j = k % n
            if i % 2:
                return (n-i-1, n-j-1)
            else:
                return (n-i-1, j)
        while q:
            k = q.popleft()
            step = d[k] + 1
            # print(k, location(k), step)
            if k == n*n:
                return d[k]
            for dice in range(6):
                k += 1
                if k > n * n:
                    break
                i, j = location(k)
                kk = board[i][j] if board[i][j] > -1 else k
                if kk not in d:
                    d[kk] = step
                    q.append(kk)
        return -1
