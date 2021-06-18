class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        def judge(k, a):
            # print(f'judge({k}, {a})')
            s = 0
            for i in range(k):
                s *= a
                s += 1
                if s > n:
                    return i, None
            return (0, a) if s == n else (-1, None)

        for k in range(62, 1, -1):
            l = 1
            r = n
            while l < r - 1:
                m = l + r >> 1
                result, a = judge(k, m)
                if result == 0:
                    return str(a)
                if result == -1:
                    l = m
                else:
                    r = m
        return ""
            
