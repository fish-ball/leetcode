class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        for h in houses:
            i = bisect.bisect_left(heaters, h)
            k = 10**9
            if i < len(heaters):
                k = min(k, abs(heaters[i]-h))
            if i > 0:
                k = min(k, abs(heaters[i-1]-h))
            ans = max(ans, k)
        return ans
