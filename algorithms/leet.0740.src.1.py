class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        a = 0  # 选中 last 的最大得分
        b = 0  # 不选中 last 的最大得分
        last = -1
        for val, cnt in sorted(Counter(nums).items()):
            aa = (b if val == last + 1 else max(a, b)) + val * cnt
            bb = max(a, b)
            a, b = aa, bb
            last = val
        return max(a, b)
        
