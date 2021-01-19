class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i):
                edges.append((abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]), (i, j)))
        edges.sort()
        ans = 0
        p = [-1] * n
        
        def find(v):
            if p[v] == -1:
                return v
            p[v] = find(p[v])
            return p[v]
        
        def merge(v, w):
            v = find(v)
            w = find(w)
            if v == w:
                return 0
            p[v] = w
            return 1
        
        k = n
        for x, (i, j) in edges:
            if merge(i, j):
                ans += x
                k -= 1
            if k <= 1:
                break
        return ans
            
