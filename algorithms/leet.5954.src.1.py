class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        a = 0
        b = n-1
        aa = capacityA
        bb = capacityB
        ans = 0
        while a < b:
            if plants[a] > aa:
                aa = capacityA
                ans += 1
            aa -= plants[a]
            a += 1
            if plants[b] > bb:
                bb = capacityB
                ans += 1
            bb -= plants[b]
            b -= 1
        if a == b  and plants[b] > max(aa, bb):
            ans += 1
        return ans
