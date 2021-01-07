class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # Floyed
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if isConnected[i][k] and isConnected[k][j]:
                        isConnected[i][j] = 1
        # 查询分块
        a = [False] * n
        k = 0
        for i in range(n):
            y = False
            for j in range(n):
                if isConnected[i][j]:
                    if not a[j]:
                        y = True
                    a[j] = True
            if y:
                k += 1
        return k
                
