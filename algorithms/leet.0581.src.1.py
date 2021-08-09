class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n - 1 and nums[i] <= nums[i+1]:
            i += 1
        p = i
        while i < n:
            while p >= 0 and nums[p] > nums[i]:
                p -= 1
            i += 1
        j = n - 1
        while j > 0 and nums[j] >= nums[j-1]:
            j -= 1
        q = j
        while j >= 0:
            while q < n and nums[j] > nums[q]:
                q += 1
            j -= 1
        # print(p,q)
        # print(nums[p+1:q])
        return max(q-p-1, 0)
