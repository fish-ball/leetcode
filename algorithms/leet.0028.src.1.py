class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n-m+1):
            yes = True
            for j in range(m):
                if needle[j] != haystack[i+j]:
                    yes = False
                    break
            if yes:
                return i
        return -1
