class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = 1<<10
        d = {i: n if i else 0 for i in range(m)}
        for i in range(k):
            # print(f'i = {i}')
            h = (n-i-1) // k + 1
            t2 = min(d.values())
            dd = {j: t2 + h for j in range(m)}
            for x, c in Counter(nums[i::k]).items():
                # print(x, c)
                for mask in range(m):
                    if dd[x^mask] > d[mask] + h - c:
                        dd[x^mask] = d[mask] + h - c
            # print(dd)
            d = dd
        return d[0]
