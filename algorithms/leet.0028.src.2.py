""" KMP 算法实现 """
class Solution:
    def compute_next(self, p):
        m = len(p)
        k = 0
        nxt = [0] * m
        # print(list(range(m)))
        # print(', '.join(p))
        # print(f'i\tk\tnxt[i]')
        for i in range(1, m):
            # print(i, end='\t')
            while k > 0 and p[k] != p[i]:
                k = nxt[k-1]
            if p[k] == p[i]:
                k += 1
            nxt[i] = k
            # print(f'{k}\t{nxt[i]}')
        return nxt

    def strStr(self, haystack: str, needle: str) -> int:
        nxt = self.compute_next(needle)
        # print(nxt)
        n = len(haystack)
        m = len(needle)
        i = 0
        j = 0
        while i <= n - m:
            if haystack[i+j] == needle[j]:
                j += 1
                if j == m:
                    return i
            elif j == 0:
                i += 1
            else:
                i += j - nxt[j-1]
                j = nxt[j-1]
            # print(i, j)
        return -1
