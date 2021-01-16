class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        p = [-1] * (n*m + 1)
        q = [0] * (n*m + 1)
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        def find(k):
            if p[k] == -1:
                return k
            p[k] = find(p[k])
            return p[k]

        def union(u, v):
            x = find(u)
            y = find(v)
            if x != y:
                p[x] = y
                q[y] += q[x]
            return q[y]

        # 断开所有标记块
        for i, (u, v) in enumerate(hits):
            if grid[u][v]:
                grid[u][v] = 0
            else:
                hits[i] = (-1, -1)

        # 初始化权重
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    q[i*m+j] = 1

        # 合并第一行
        for j in range(m):
            union(j, n*m)

        def group(u, v):
            grid[u][v] = 0
            for xx, yy in zip(dx, dy):
                x = u + xx
                y = v + yy
                if 0 <= x < n and 0 <= y < m and grid[x][y]:
                    group(x, y)
                    union(x*m+y, u*m+v)
        
        # 合并其他
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    group(i, j)
        
        ans = []   

        for u, v in hits[::-1]:
            if u < 0:
                ans.append(0)
                continue
            cnt = 0
            s1 = set() # 连到屋顶的集合
            s2 = set() # 不连到屋顶的集合
            for xx, yy in zip(dx, dy):
                x = u + xx
                y = v + yy
                if 0 <= x < n and 0 <= y < m: 
                    w = find(x*m+y)
                    if not q[x*m+y]:
                        continue
                    if w == find(n*m):
                        s1.add(w)
                    else:
                        s2.add(w)
            if u == 0 or s1:
                # 有相连，说明不是孤点
                ans.append(sum([q[w] for w in s2]))
                q[u*m+v] = 1
                for w in s1 | s2:
                    union(w, u*m+v)
            else:
                # 否则说明是孤点
                ans.append(0)
                q[u*m+v] = 1
                for w in s2:
                    union(w, u*m+v)

        return ans[::-1]
