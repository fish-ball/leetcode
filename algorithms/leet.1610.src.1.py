class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        a = []
        ans = 0
        EPS = 1e-6
        for x, y in points:
            x -= location[0]
            y -= location[1]
            if x == 0 and y == 0:
                ans += 1
                continue
            elif x == 0 and y > 0:
                ag = math.pi/2
            elif x == 0 and y < 0:
                ag = 3*math.pi/2
            elif y == 0 and x > 0:
                ag = 0
            elif y == 0 and x < 0:
                ag = math.pi
            else:
                ag = math.atan2(y, x) + 2*math.pi
            a.append((ag/pi*180+360)%360)
        a.sort()
        q = Deque([])
        mx = 0
        a += [x + 360 for x in a]
        # print(ans, a)
        for ag in a:
            while q and q[0]<ag-angle-EPS:
                q.popleft()
            q.append(ag)
            # print(ag, [x%360 for x in q])
            # print(len(q))
            mx = max(mx, len(q))
        return ans + mx
