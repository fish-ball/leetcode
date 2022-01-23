class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S') & 1 or 'S' not in corridor:
            return 0
        arr = []
        p = 0
        s = 0
        for x in corridor:
            if x == 'S':
                if s == 0:
                    if p:
                        arr.append(p)
                        p = 0
                    s = 1
                elif s == 1:
                    s = 0
                    p = 0
            elif x == 'P':
                if s == 0:
                    p += 1
        if corridor[0] == 'P' and arr:
            arr.pop(0)
        ans = 1
        # print(arr)
        for x in arr:
            ans *= x+1
            ans %= 1000000007
        return ans
        
                
