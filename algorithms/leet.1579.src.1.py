class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        e1 = []
        e2 = []
        e3 = []
        ee = [e1, e2, e3]
        for t, x, y in edges:
            ee[t-1].append((x-1, y-1))
        ans = 0
        p = list(range(n))

        c1 = n
        c2 = n

        def find(x):
            if p[x] == x:
                return x
            p[x] = find(p[x])
            return p[x]


        for x, y in e3:
            x = find(x)
            y = find(y)
            if x == y:
                ans += 1
            else:
                p[x] = y
                c1 -= 1
                c2 -= 1
        
        # print(c1, c2, p)

        p0 = p[:]

        for x, y in e1:
            x = find(x)
            y = find(y)
            if x == y:
                ans += 1
            else:
                p[x] = y
                c1 -= 1

        p = p0

        for x, y in e2:
            x = find(x)
            y = find(y)
            if x == y:
                ans += 1
            else:
                p[x] = y
                c2 -= 1

        return ans if c1 == 1 and c2 == 1 else -1
