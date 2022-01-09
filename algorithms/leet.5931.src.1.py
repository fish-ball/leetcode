class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        for row in grid:
            row.append(1)
        grid.append([1] * len(grid[0]))
        m = len(grid)
        n = len(grid[0])
        la = [-1] * n
        # for row in grid:
        #     print(row)
        # print()
        for row in grid:
            last = -1
            i = 0
            while i < n:
                if row[i] == 1:
                    if last > -1 and i - last < stampWidth:
                        return False
                    if la[i] > -1 and la[i] < stampHeight:
                        return False
                    la[i] = -1
                else:
                    if last == -1:
                        last = i
                    if la[i] == -1:
                        la[i] = 1
                        j = i-1
                        while j > i-stampWidth and j >= 0 and la[j] > 1:
                            la[j] = 1
                            j -= 1
                        j = i+1
                        while j < i+stampWidth and j < n and la[j] > 1 and row[j] == 0:
                            la[j] = 1
                            j += 1
                        i = j
                        continue
                    else:
                        la[i] += 1
                i += 1
        #     print(la)
        # print()
        return True
                        
                        
                    
                
