class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[-1] == '1':
            return False
        ii = deque([i for i, c in enumerate(s) if c == '0'])
        qq = deque([n-1])
        while qq:
            # print(qq, ii)
            x = qq.popleft()
            if x == 0:
                return True
            while ii and ii[-1] > x - minJump:
                ii.pop()
                # print(ii)
            while ii and ii[-1] >= x - maxJump:
                # y = ii.pop()
                qq.append(ii.pop())
                
                # print(ii)
        return False
