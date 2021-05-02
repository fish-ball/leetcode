class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        c = Counter()
        for line in wall:
            acc = 0
            for x in line[:-1]:
                acc += x
                c.subtract({acc: -1})
        return len(wall) - (max(c.values()) if c else 0)
