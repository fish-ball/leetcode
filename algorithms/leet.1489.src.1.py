class Solution:
    def bst(self, n, edges):
        p = list(range(n))
        def find(x):
            if p[x] == x:
                return x
            p[x] = find(p[x])
            return p[x]
        ans = 0
        for w, x, y, k in edges:
            x0=x
            y0=y
            x = find(x)
            y = find(y)
            if x != y:
                n -= 1
                ans += w
                p[x] = y
            if n <= 1:
                return ans
        return -1

    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        a = []
        b = []
        mn = self.bst(n, sorted([(w, x, y, i) for i, (x, y, w) in enumerate(edges)]))

        for k, (x0, y0, w0) in enumerate(edges):
            ee = sorted([(w, x, y, i) for i, (x, y, w) in enumerate(edges) if i != k])
            val = self.bst(n, ee)
            if val > mn or val == -1:
                a.append(k)
                continue
            val = self.bst(n, [(w0, x0, y0, k)] + ee)
            if val == mn:
                b.append(k)
        
        return [a, b]
