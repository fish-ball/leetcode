class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if target == source:
            return 0
        n = len(routes)
        g = [set() for i in range(n)]
        d = {}
        t = set()
        for i, v in enumerate(routes):
            for k in v:
                if k == target:
                    t.add(i)
                if k not in d:
                    d[k] = set()
                for j in d[k]:
                    g[i].add(j)
                    g[j].add(i)
                d[k].add(i)
        # for row in g:
        #     print(row)
        # print(t)
        b = [-1] * n
        q = deque([])
        for i in d[source]:
            b[i] = 1
            q.append(i)
        while q:
            i = q.popleft()
            s = b[i]
            if i in t:
                return s
            for j in g[i]:
                if b[j] == -1:
                    b[j] = s + 1
                    q.append(j)
        return -1
