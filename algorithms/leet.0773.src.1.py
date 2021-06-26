class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = (*board[0], *board[1])
        d = {s: 0}
        q = Deque([s])
        while q:
            s = q.popleft()
            k = d[s]
            # print(f'k = {k}\n', *s[:3], '\n', *s[3:])
            if s == (1, 2, 3, 4, 5, 0):
                return k
            for i, x in enumerate(s):
                if x:
                    continue
                for dd in (-1, 1, 3, -3):
                    if i == 3 and dd == -1 or i == 2 and dd == 1:
                        continue
                    if not 0 <= i + dd < 6:
                        continue
                    j = i + dd
                    v = list(s)
                    v[i], v[j] = v[j], v[i]
                    v = tuple(v)
                    if v in d:
                        continue
                    d[v] = k + 1
                    q.append(tuple(v))
        return -1
