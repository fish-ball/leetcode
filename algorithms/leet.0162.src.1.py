class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n
        while l < r - 1:
            m = l + r >> 1
            # print(l, r, m)
            if (m<=0 or nums[m]<nums[m-1]):
                r = m
            elif (m>=n-1 or nums[m]<nums[m+1]):
                l = m
            else:
                return m
        return l
