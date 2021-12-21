class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        return ' '.join([s[a:b] for a, b in zip([0]+spaces, spaces+[len(s)])])
