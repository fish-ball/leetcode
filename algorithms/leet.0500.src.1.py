class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        kk = [
            'qwertyuiop',
            'asdfghjkl',
            'zxcvbnm'
        ]
        d = {}
        for i in range(3):
            for c in kk[i]:
                d[c] = i
        ans = []
        for w in words:
            dd = set()
            for c in w:
                dd.add(d[c.lower()])
            if len(dd) == 1:
                ans.append(w)
        return ans
