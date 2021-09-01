class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        v1 += [0] * max(len(v2)-len(v1), 0)
        v2 += [0] * max(len(v1)-len(v2), 0)
        return 1 if v1 > v2 else -1 if v1 < v2 else 0
