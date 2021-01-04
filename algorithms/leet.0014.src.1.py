class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        a = ''
        for s in zip(*strs):
            print(s)
            if len(set(s)) != 1:
                break
            a += s[0]
        return a
