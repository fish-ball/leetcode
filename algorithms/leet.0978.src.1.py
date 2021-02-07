class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        acc = 1
        ans = 1
        n = len(arr)
        d = 0
        for i in range(1, n):
            if arr[i] > arr[i-1]:
                if d == -1:
                    acc += 1
                else:
                    acc = 2
                d = 1
            elif arr[i] < arr[i-1]:
                if d == 1:
                    acc += 1
                else:
                    acc = 2
                d = -1
            else:
                acc = 1
                d = 0
            ans = max(ans, acc)
        return ans

