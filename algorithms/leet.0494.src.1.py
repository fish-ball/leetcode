class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - target
        if target < 0 or target % 2 == 1:
            return 0
        target //= 2
        d = [0] * (target + 1)
        d[0] = 1
        for c in nums:
            for i in range(target, c - 1, -1):
                d[i] += d[i-c]
            # print(d)
        return d[target]
