class Solution:
    def sortSentence(self, s: str) -> str:
        d = dict()
        for w in s.split():
            k = int(w[-1]) - 1
            d[k] = w[:-1]
        # print(d)
        return ' '.join([v for k, v in sorted(d.items())])
