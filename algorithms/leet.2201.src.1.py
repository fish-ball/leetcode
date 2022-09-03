class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        s = {(x, y) for x, y in dig}
        ans = 0
        for x1, y1, x2, y2 in artifacts:
            yes = True
            for i in range(x1, x2+1):
                for j in range(y1,y2+1):
                    if (i,j) not in s:
                        yes = False
            if yes:
                ans += 1
        return ans
