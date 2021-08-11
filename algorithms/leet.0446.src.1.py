class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        g = [{} for i in range(n)]
        ans = 0
        for j in range(n):
            y = nums[j]
            for i in range(j):
                x = nums[i]
                d = y - x
                # print(f'g[x] = {g[x]}, d = {d}, {g[x].get(d)}')
                g[j][d] = g[j].get(d, 0)
                g[j][d] += g[i].get(d, 0) + 1
                ans += g[i].get(d, 0)
            # print(f'y = {y}')
            # print(g)
        return ans
