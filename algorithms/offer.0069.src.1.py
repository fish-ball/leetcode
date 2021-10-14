class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l = -1
        r = n + 1
        k = 1000
        while l + 2 < r:
            m1 = (l * 2 + r) // 3
            m2 = (l + r * 2) // 3
            if arr[m1] > arr[m2]:
                r = m2
            else:
                l = m1
        return l + 1
