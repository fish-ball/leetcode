class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        pos = 0
        while k and pos > -1:
            pos = s.find(' ', pos+1)
            k -= 1
        return s[:pos] if pos > -1 else s
