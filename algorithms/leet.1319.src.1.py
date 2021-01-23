class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        p = list(range(n))

        def find(x):
            if p[x] == x:
                return x
            p[x] = find(p[x])
            return p[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x != y:
                p[x] = y
        
        for v, w in connections:
            union(v, w)

        return len(set([find(x) for x in p])) - 1 \
            if len(connections) >= n-1 else -1
