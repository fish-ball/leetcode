class Solution:
    def nextStr(self, s):
        last = ''
        cnt = 0
        ans = ''
        for c in s:
            if c == last:
                cnt += 1
            else:
                if cnt > 0:
                    ans += f'{cnt}{last}'
                cnt = 1
                last = c
        if cnt > 0:
            ans += f'{cnt}{last}'
        return ans

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        return self.nextStr(self.countAndSay(n-1))
