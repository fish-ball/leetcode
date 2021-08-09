class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        def calc(x):
            mp = {(x, 1<<x): 0}
            q = Deque([(x, 1<<x)])
            while q:
                v, mask = q.popleft()
                k = mp[(v, mask)]
                if mask == (1<<n)-1:
                    return k
                for w in graph[v]:
                    mask1 = mask | (1<<w)
                    if (w, mask1) not in mp:
                        mp[(w, mask1)] = k + 1
                        q.append((w, mask1))
            return n*n
        return min([calc(k) for k in range(n)])
