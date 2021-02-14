class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2
        g = [set() for i in range(n)]
        for i in range(n):
            v = row[i+i] // 2
            w = row[i+i+1] // 2
            g[v].add(w)
            g[w].add(v)
        ans = 0
        b = [False] * n

        def dfs(v):
            if b[v]:
                return 0
            b[v] = True
            for w in g[v]:
                if not b[w]:
                    return dfs(w) + 1
            return 0

        for i in range(n):
            ans += dfs(i)
        return ans
