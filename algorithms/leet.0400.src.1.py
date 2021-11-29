class Solution:
    def findNthDigit(self, n: int) -> int:
        '''
        1-9: 9
        10-99: 90
        100-999:900
        1000-9999: 9000
        '''
        p = 1
        k = 9
        while n > k*p:
            n -= k*p
            p += 1
            k *= 10
        n -= 1
        # print(10**(p-1), n//p, n%p)
        return int(str(10**(p-1)+n//p)[n%p])
