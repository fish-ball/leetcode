class Solution:
    def permutation(self, s: str) -> List[str]:
        n = len(s)
        arr = sorted(s)
        ans = []
        while True:
            ans.append(''.join(arr))
            i = n - 1
            while i > 0 and arr[i-1] >= arr[i]:
                i -= 1
            if i == 0:
                break
            i -= 1
            j = i
            while j + 1 < n and arr[j+1] > arr[i]:
                j += 1
            # print(arr, i, j)
            arr[i], arr[j] = arr[j], arr[i]
            arr[i+1:] = arr[i+1:][::-1]
        return ans
