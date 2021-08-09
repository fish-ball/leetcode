class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        # e 记录在每个不同的 x，有多少种合并操作，操作 {y: -k} 代表在 x, y 出弹出 k 次，{y: k} 代表在 x, y 处压入 k 次
        e = {}
        for x1, x2, y in buildings:
            if x1 not in e:
                e[x1] = {}
            if x2 not in e:
                e[x2] = {}
            e[x1][y] = e[x1].get(y, 0) + 1
            if e[x1][y] == 0:
                del e[x1][y]
            e[x2][y] = e[x2].get(y, 0) - 1
            if e[x2][y] == 0:
                del e[x2][y]
        buf = {}
        y0 = 0
        h = []
        # 从小到大遍历 x，对于每个不同的 x，记录当前（最大堆）内的所有 y，只需要看最大的值是多少
        for x in sorted(e.keys()):
            # print(x, e[x])
            # 要首先将 x 处的所有压入、弹出在堆上进行处理，buf 是用于缓冲非堆顶弹出的记录
            for y, d in e[x].items():
                while d > 0:
                    heapq.heappush(h, -y)
                    d -= 1
                if d < 0:
                    buf[-y] = buf.get(-y, 0) - d
            # 如果堆顶的元素在缓冲区 buf 里面有，则弹出，直到堆顶的元素的确为幸存值
            while h and h[0] in buf:
                y = -heapq.heappop(h)
                buf[-y] -= 1
                if buf[-y] == 0:
                    del buf[-y]
            # print(h, buf)
            # 这个时候，如果堆已经空，说明该点的天际线高度到达地平线 y=0，否则堆顶值即为该 x 值的天际线高度，输出
            y = -h[0] if h else 0
            # 只有当天际线高度发生变动的时候，才输出一个
            if y != y0:
                y0 = y
                ans.append((x, y0))
        return ans
