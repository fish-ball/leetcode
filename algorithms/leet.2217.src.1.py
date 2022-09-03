class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        b = int(10**((intLength-1)//2))
        # print(f'b = {b}')
        def gao(k):
            x = b + k - 1
            s = str(x)
            if len(s) > len(str(b)):
                return -1
            ss = s[::-1]
            return s+ss[1:] if intLength&1 else s+ss
        return [
            int(gao(k)) for k in queries
        ]
