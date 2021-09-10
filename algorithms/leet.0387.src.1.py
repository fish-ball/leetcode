class Solution:
    def firstUniqChar(self, s: str) -> int:
        ct = Counter(s)
        for i, c in enumerate(s):
            if ct[c] == 1:
                return i
        return -1
        
