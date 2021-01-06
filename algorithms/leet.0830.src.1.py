class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        a = -1
        c = ''
        result = []
        for i, x in enumerate(s+'~'):
            if c != x:
                if i - a >= 3:
                    result.append([a, i-1])
                a = i
                c = x
        return result
