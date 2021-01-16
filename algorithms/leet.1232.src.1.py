class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        for x, y in coordinates[2:]:
            if (x1-x2)*(y1-y) != (x1-x)*(y1-y2):
                return False
        return True
