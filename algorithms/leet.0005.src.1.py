class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        mx = 0
        ans = ''
        for i, x in enumerate(s):
            k = 0
            while i-k>=0 and i+k<n and s[i-k] == s[i+k]:
                if k+k+1 > mx:
                    mx = k+k+1
                    ans = s[i-k:i+k+1]
                k += 1
            k = 0
            while i-k>=0 and i+k+1<n and s[i-k] == s[i+k+1]:
                if k+k+2 > mx:
                    mx = k+k+2
                    ans = s[i-k:i+k+2]
                k += 1
        return ans
