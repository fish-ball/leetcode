class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(m, n):
            return gcd(n, m%n) if n else m
        n = len(points)
        mp = {}
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                y2 -= y1
                x2 -= x1
                a = y2
                b = -x2
                c = x2*y1 - x1*y2
                g = gcd(gcd(a, b), c)
                a /= g
                b /= g
                c /= g
                if a < 0:
                    a, b, c = -a, -b, -c
                t = (a, b, c)
                mp[t] = mp.get(t, 0) + 1
                ans = max(ans, mp[t])
        return int((ans * 2) ** .5) + 1
