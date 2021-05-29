class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        ans =  []
        n = len(grid)
        m = len(grid[0])
        
        d1 = [] # 副对角线（右上）
        for i in range(n+m-1):
            row = [0]
            for j in range(m):
                row.append(row[-1])
                ii = i - j
                if ii >= 0 and ii < n:
                    row[-1] += grid[ii][j]
            d1.append(row)
            
        d2 = [] # 主对角线（右下）
        for i in range(n+m-1):
            row = [0]
            for j in range(m):
                row.append(row[-1])
                ii = i - m + j + 1
                if ii >= 0 and ii < n:
                    row[-1] += grid[ii][j]
            d2.append(row)
            
        # for row in d1:
        #     print(row)
        # print('-----')
        # for row in d2:
        #     print(row)
                
        def calc(i, j, k):
            # print(f'calc({i}, {j}, {k})')
            if k == 0:
                return grid[i][j]
            a1 = d1[i+j+k//2][j+k//2+1] - d1[i+j+k//2][j]
            a2 = d1[i+j+k+k//2][j+k+1] - d1[i+j+k+k//2][j+k//2]
            b1 = d2[i-j+m-1-k//2][j+k+1] - d2[i-j+m-1-k//2][j+k//2]
            b2 = d2[i-j+m-1+k//2][j+k//2+1] - d2[i-j+m-1+k//2][j]
            # print(a1, a2, b1, b2)
            return a1 + a2 + b1 + b2 \
                - grid[i+k//2][j] \
                - grid[i][j+k//2] \
                - grid[i+k][j+k//2] \
                - grid[i+k//2][j+k]
            
        for i in range(n):
            for j in range(m):
                for k in range(0, min(n-i, m-j), 2):
                    val = calc(i, j, k)
                    # print(f'val = {val}')
                    ans.append(val)
                    ans = sorted(set(ans), reverse=True)[:3]
        return ans
