class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        for _, ss in sorted(zip(map(lambda x: (-len(x), x), dictionary), dictionary)):
            i = 0
            for c in s:
                if i < len(ss) and ss[i] == c:
                    i += 1
            if i == len(ss):
                return ss
        return ''
