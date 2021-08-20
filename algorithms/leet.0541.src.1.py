class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        ss = list(s)
        for i in range(0, n, k+k):
            j = min(i+k, n)
            ss[i:j] = ss[i:j][::-1]
        return ''.join(ss)
