class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = []
        for x, y in zip(s1, s2):
            if x != y:
                diff.append((x, y))
        return not diff or len(diff) == 2 and diff[0] == diff[1][::-1]
