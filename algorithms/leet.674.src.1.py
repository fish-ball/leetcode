class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1 if nums else 0
        k = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                if i - k + 1 > ans:
                    ans = i - k + 1
            else:
                k = i
            print(i, k, ans)
        return ans
