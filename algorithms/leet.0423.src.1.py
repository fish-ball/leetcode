class Solution:
    def originalDigits(self, s: str) -> str:
        ws = [
            ('z', '0', 'zero'),
            ('x', '6', 'six'),
            ('g', '8', 'eight'),
            ('h', '3', 'three'),
            ('u', '4', 'four'),
            ('s', '7', 'seven'),
            ('f', '5', 'five'),
            ('w', '2', 'two'),
            ('o', '1', 'one'),
            ('e', '9', 'nine')
        ]
        ans = Counter()
        pool = Counter(s)
        for k, d, w in ws:
            n = pool.get(k) or 0
            pool -= Counter(w * n)
            ans += {d: n}
        return ''.join(sorted(ans.elements()))
