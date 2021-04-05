class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        def dec2tri(x):
            if x < 0:
                return [-v for v in dec2tri(-x)]
            a = [0] * 32
            i = 0
            while x > 0:
                rem = x % 3
                x //= 3
                if rem == 2:
                    rem = -1
                    x += 1
                a[i] = rem
                i += 1
            return a

        bits = [0] * 32
        for x in nums:
            # print(x, dec2tri(x))
            for i, v in enumerate(dec2tri(x)):
                bits[i] += v + 6
                bits[i] %= 3
                if bits[i] == 2:
                    bits[i] = -1

        ans = 0
        for c in bits[::-1]:
            ans *= 3
            ans += c
        return ans
