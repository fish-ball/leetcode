class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        c = False
        for l, r in sorted(ranges):
            if not c and l > left:
               return False
            if l > left + 1:
                return False
            if r >= left:
                c = True
            left = max(left, r)
        return c and left >= right
