class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        last = 'L'
        rn = 0
        for c in directions:
            if c == 'L':
                if last == 'R':
                    ans += rn + 1
                    last = 'S'
                elif last == 'S':
                    ans += 1
                rn = 0
            elif c == 'R':
                last = 'R'
                rn += 1
            elif c == 'S':
                if last == 'R':
                    ans += rn
                last = 'S'
                rn = 0
                    
            # print(c, ans)
        return ans
            
