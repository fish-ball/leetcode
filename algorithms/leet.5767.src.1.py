class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left, right+1):
            yes = False
            for l, r in ranges:
                if l <= x <= r:
                    yes = True
                    break
            if not yes:
                return False
        return True
            
