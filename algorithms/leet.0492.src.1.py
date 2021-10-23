class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a = 1
        for i in range(1, area):
            if i * i > area:
                break
            if area % i == 0:
                a = i
        return [area // a, a]
