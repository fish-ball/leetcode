class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ans = 0
        d = {}
        core = False
        for w in words:
            d[w] = d.get(w, 0) + 1
        for k in words:
            while k in d:
                d[k] -= 1
                if d[k] == 0:
                    del d[k]
                kk = k[::-1]
                if kk in d:
                    ans += 4
                    d[kk] -= 1
                    if d[kk] == 0:
                        del d[kk]
                elif k == kk:
                    core = True
            
        return ans + (2 if core else 0)
