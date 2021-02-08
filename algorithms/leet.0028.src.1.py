class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(haystack)
        m = len(needle)
        for i in range(n-m+1):
            fail = False
            for j in range(m):
                if needle[j] != haystack[i+j]:
                    fail = True
            if not fail:
                return i
        return -1
