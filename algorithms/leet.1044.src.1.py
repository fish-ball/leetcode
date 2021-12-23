class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        ans = (0, 0)
        l = 0
        r = n+1
        MOD = 1000000000000007
        pw = [1]

        for i in range(n):
            pw.append(pw[-1]*26%MOD)
        nums = [ord(x) - ord('a') for x in s]
        def well(m):
            hs = {}
            acc = 0
            for i in range(m):
                acc = (acc * 26 + nums[i]) % MOD
                
            hs[acc] = 0
            for i in range(m, n):
                j = i - m
                acc = (acc - pw[m-1]*nums[j]%MOD + MOD) % MOD
                acc = (acc * 26 + nums[i]) % MOD
                if acc in hs:
                    return (j+1, i+1)
                hs[acc] = j+1

        while l < r-1:
            m = l + r >> 1
            better = well(m)
            if better:
                l = m
                ans = better
            else:
                r = m
        return s[ans[0]:ans[1]]
