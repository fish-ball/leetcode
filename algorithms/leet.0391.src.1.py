class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        rectangles.sort()
        xs, ys, x2s, y2s = zip(*rectangles)
        q = [(min(xs), min(ys), max(y2s))]
        area = (max(y2s)-min(ys)) * (max(x2s)-min(xs))
        for x, y, a, b in rectangles:
            area -= (b-y) * (a-x)
            xx, y1, y2 = heappop(q)
            while q and q[0][0] == xx and q[0][1] == y2:
                *_, y2 = heappop(q)
            if (x, y) != (xx, y1) or b > y2:
                return False
            if b < y2:
                heappush(q, (x, b, y2))
            heappush(q, (a, y, b))
        return area == 0
