class Solution:
    def countElements(self, nums: List[int]) -> int:
        p = sorted(Counter(nums).items())
        ans = 0
        for i, (x, n) in enumerate(p):
            if i == 0 or i == len(p) - 1:
                continue
            # if p[i-1][1] == 1 and p[i+1][1] == 1:
            ans += n
        return ans
