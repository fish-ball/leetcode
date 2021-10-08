class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        dd = dict(A=0, C=1, G=2, T=3)
        acc = 0
        cnt = {}
        ans = []
        m = (1<<20)-1
        for i, c in enumerate(s):
            acc <<= 2
            acc += dd[c]
            acc &= m
            if i < 9:
                continue
            cnt[acc] = cnt.get(acc, 0) + 1
            if cnt[acc] == 2:
                ans.append(s[i-9:i+1])
        return ans
