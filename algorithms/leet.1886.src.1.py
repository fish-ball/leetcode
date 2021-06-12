class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            # print(mat, target)
            yes = True
            for x, y in zip(mat, target):
                if list(x) != list(y):
                    yes = False
            if yes:
                return True
            mat = list(zip(*mat[::-1]))
        return False
