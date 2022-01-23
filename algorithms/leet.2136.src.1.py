class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = 0
        t = 0
        for g, p in sorted(zip(growTime, plantTime), reverse=True):
            t += p
            ans = max(ans, t+g)
            # print(g, p, t, ans)
        # print()
        return ans
