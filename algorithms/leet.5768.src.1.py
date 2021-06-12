class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        s = sum(chalk)
        k %= s
        for i, x in enumerate(chalk):
            if k < x:
                return i
            k -= x
        return 0
