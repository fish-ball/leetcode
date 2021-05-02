class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for x, y in sorted(intervals):
            if not ans or ans[-1][1] < x:
                ans.append([x, y])
            else:
                ans[-1][1] = max(ans[-1][1], y)
        return ans
