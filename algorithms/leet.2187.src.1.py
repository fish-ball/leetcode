class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = min(time) * totalTrips
        while l < r-1:
            m = l+r>>1
            c = sum(m // t for t in time)
            if c < totalTrips:
                l = m
            else:
                r = m
        return r
