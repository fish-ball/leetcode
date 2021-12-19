class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        c = [0] * n
        d = [0] * n
        for a, b in trust:
            c[a-1] += 1
            d[b-1] += 1
        judger = -2
        for i in range(n):
            if c[i] == 0 and d[i] == n-1:
                if judger > -1:
                    return -1
                judger = i
        return judger+1
