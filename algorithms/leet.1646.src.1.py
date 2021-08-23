class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        d = [0, 1]
        for i in range(2, n+1):
            if i & 1:
                d.append(d[i//2]+d[i//2+1])
            else:
                d.append(d[i//2])
        return max(d[:n+1])
