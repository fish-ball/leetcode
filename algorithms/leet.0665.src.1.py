class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        k = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                k += 1
                if k > 1:
                    return False
                if i == 1:
                    nums[0] = nums[1]
                elif nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
        return True
