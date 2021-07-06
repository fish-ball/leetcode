class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        for c in sorted(costs):
            coins -= c
            if coins < 0:
                break
            ans += 1
        return ans
