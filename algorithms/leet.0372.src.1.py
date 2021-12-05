class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def pp(a, b):
            if not b:
                return 1
            d = (pp(a, b>>1) ** 2) % 1337
            return d*a%1337 if b&1 else d
        return pp(a, int(''.join(map(str, b))))
