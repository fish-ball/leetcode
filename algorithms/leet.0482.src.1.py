class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '')[::-1].upper()
        ans = ''
        while s:
            ans += '-' + s[:k]
            s = s[k:]
        return ans[:0:-1]
