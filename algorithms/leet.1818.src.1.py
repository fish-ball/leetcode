class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        a = sorted(nums1)
        mx = 0
        ans = 0
        for i in range(n):
            diff = abs(nums1[i] - nums2[i])
            ans += diff
            ans %= 1000000007
            j = bisect.bisect_left(a, nums2[i])
            if j < n:
                x = diff-abs(nums2[i]-a[j])
                if mx < x:
                    mx = x
            if j > 0:
                x = diff-abs(nums2[i]-a[j-1])
                if mx < x:
                    mx = x
        ans -= mx
        ans += 1000000007
        ans %= 1000000007
        return ans
