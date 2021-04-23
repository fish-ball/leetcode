class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [-1] * n
        cnt = [1] * n
        arr = sorted(nums)
        mx = 0
        mxi = 0
        for i, x in enumerate(arr):
            for j in range(0, i):
                y = arr[j]
                if x % y == 0 and cnt[i] < cnt[j] + 1:
                    cnt[i] = cnt[j] + 1
                    pre[i] = j
                    if cnt[i] > mx:
                        mxi = i
                        mx = cnt[i]
        ans = []
        while mxi > -1:
            ans.append(arr[mxi])
            mxi = pre[mxi]
        return ans[::-1]
