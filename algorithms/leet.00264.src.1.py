class Solution:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        d = [1]
        i = j = k = 0
        for n in range(1700):
            ti = d[iac] * 2
            tj = d[j] * 3
            tk = d[k] * 5
            tt = min(ti, tj, tk)
            if ti == tt:
                i += 1
            if tj == tt:
                j += 1
            if tk == tt:
                k += 1
            d.append(tt)
        self.d = d

    def nthUglyNumber(self, n: int) -> int:
        return self.d[n-1]
        
