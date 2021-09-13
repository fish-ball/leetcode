class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0
        for i, (x, y) in enumerate(points):
            c = {}
            for j, (xx, yy) in enumerate(points):
                if i == j:
                    continue
                k = (x-xx)*(x-xx)+(y-yy)*(y-yy)
                c[k] = c.get(k, 0) + 1
            # print(c)
            for v in c.values():
                if v >= 2:
                    ans += v * (v-1)
        return ans
