class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        if numerator < 0 and denominator < 0:
            return self.fractionToDecimal(-numerator, -denominator)
        if numerator < 0 or denominator < 0:
            return '-' + self.fractionToDecimal(abs(numerator), abs(denominator))
        ans = str(numerator//denominator) + '.'
        numerator %= denominator
        rem = {numerator: len(ans)}
        while numerator:
            numerator *= 10
            ans += str(numerator // denominator)
            numerator %= denominator
            if numerator in rem:
                ans = ans[:rem[numerator]] + f'({ans[rem[numerator]:]})'
                break
            rem[numerator] = len(ans)
        return ans.strip('.')
