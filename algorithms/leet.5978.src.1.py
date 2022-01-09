class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        d = set([''.join(sorted(w)) for w in startWords])
        ans = 0
        for w in targetWords:
            ww = ''.join(sorted(w))
            for i, c in enumerate(w):
                www = ww[:i] + ww[i+1:]
                if www in d:
                    ans += 1
                    break
        return ans
