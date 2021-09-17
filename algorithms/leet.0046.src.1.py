class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        while True:
            ans.append(nums[:])
            i = n - 1
            while i > 0 and nums[i] <= nums[i-1]:
                i -= 1
            if i == 0:
                break
            j = i
            while j+1<n and nums[j+1] > nums[i-1]:
                j += 1
            # print(i, j)
            nums[i-1], nums[j] = nums[j], nums[i-1]
            nums[i:] = nums[i:][::-1]
            # print(nums)
        return ans
