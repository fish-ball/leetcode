class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        a = [0]
        for x in differences:
            a.append(a[-1]+x)
        return max(0, upper-lower -  (max(a)-min(a)) + 1)
