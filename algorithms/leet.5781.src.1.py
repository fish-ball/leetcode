class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            p = s.find(part)
            if p == -1:
                break
            s = s[:p] + s[p+len(part):]
        return s
