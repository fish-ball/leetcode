class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        d = dict()
        j = 0
        for i, x in enumerate(nums):
            if x not in d:
                d[x] = [1, -1, i]
            else:
                d[x][1] = -(i - d[x][2] + 1)
                d[x][0] += 1
        return -sorted(d.values())[-1][1]
            

