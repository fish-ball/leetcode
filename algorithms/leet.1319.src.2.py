class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        if len(connections) < n-1:
            return -1

        # 并查集
        u = list(range(n))
        k = n

        def find(x):
            if x == u[x]:
                return x
            u[x] = find(u[x])
            return u[x]

        def union(x, y):
            nonlocal k
            x = find(x)
            y = find(y)
            if x != y:
                k -= 1
            u[x] = y

        for x, y in connections:
            union(x, y)

        return k-1

