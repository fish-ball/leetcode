class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(1, n):
            arr[i] += arr[i-1]
        arr.append(0)
        for i in range(n):
            for j in range(i, n, 2):
                ans += arr[j] - arr[i-1]
        return ans
