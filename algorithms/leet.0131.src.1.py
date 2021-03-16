class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # 预计算
        g = [[False] * n for i in range(n)]
        for i in range(n):
            g[i][i] = True
        for k in range(1, n):
            for i in range(0, n-k):
                g[i][i+k] = g[i+k][i] = s[i] == s[i+k] and (True if k <= 2 else g[i+1][i+k-1])
        
        ans = []
        trc = []

        def dfs(k):
            if k == n:
                ans.append(trc[:])
                return
            for i in range(k, n):
                if g[i][k]:
                    trc.append(s[k:i+1])
                    dfs(i+1)
                    trc.pop()
        
        dfs(0)
        return ans
