class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cp = sorted(zip(capital, profits), reverse= True)
        hp = []
        while k:
            while cp and cp[-1][0] <= w:
                c, p = cp.pop()
                heapq.heappush(hp, -p)
            if not hp:
                break
            w -= heapq.heappop(hp)
            k -= 1
        return w
