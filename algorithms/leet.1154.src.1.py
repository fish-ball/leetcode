class Solution:
    def dayOfYear(self, date: str) -> int:
        y,m,d = map(int, date.split('-'))
        mm = [31,28,31,30,31,30,31,31,30,31,30,31]
        if y%400==0 or y%100 and y%4==0:
            mm[1] = 29
        ans = d
        for i in range(m-1):
            ans += mm[i]
        return ans
