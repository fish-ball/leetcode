class Solution:
    def numberToWords(self, num: int) -> str:
        if num >= 10**9:
            return (self.numberToWords(num // 10**9)
                + ' Billion ' + self.numberToWords(num % 10**9)).strip().replace(' Zero', '')
        if num >= 10**6:
            return (self.numberToWords(num // 10**6)
                + ' Million ' + self.numberToWords(num % 10**6)).strip().replace(' Zero', '')
        if num >= 10**3:
            return (self.numberToWords(num // 10**3)
                + ' Thousand ' + self.numberToWords(num % 10**3)).strip().replace(' Zero', '')
        ones = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        vens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        ans = ''
        if num >= 100:
            ans = ones[num // 100] + ' Hundred'
            num %= 100
        if num >= 20:
            ans = ans.strip() + ' ' + tens[num // 10]
            num %= 10
        if num >= 10:
            ans = ans.strip() + ' ' + vens[num-10]
            num = 0
        if num:
            ans = ans.strip() + ' ' + ones[num]
        return ans.strip() or 'Zero'
