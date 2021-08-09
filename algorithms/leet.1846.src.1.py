class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        k = 1
        for i, a in enumerate(arr):
            if a < i + k:
                k = a - i
        return n - 1 + k
