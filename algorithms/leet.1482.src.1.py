class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        l = 0
        r = max(bloomDay)
        while l + 1 < r:
            x = l + r + 1 >> 1
            kk = 0
            mm = 0
            for i, a in enumerate(bloomDay):
                if a > x:
                    kk = 0
                else:
                    kk += 1
                    if kk >= k:
                        kk = 0
                        mm += 1
                        if mm >= m:
                            break
            if mm >= m:
                r = x
            else:
                l = x
        return r
