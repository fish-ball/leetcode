class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        for x in sorted(costs):
            coins -= x
            if coins < 0:
                break
            ans += 1
        return ans
