class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        s = sum(stones)
        m = s // 2
        d = [False] * (m + 1)
        d[0] = True
        mx = 0
        for x in stones:
            for i in range(m, x-1, -1):
                d[i] = d[i] or d[i-x]
                if d[i]:
                    mx = max(mx, i)
            # print(''.join(['1' if c else '0' for c in d]))
        return abs(s-mx-mx)
