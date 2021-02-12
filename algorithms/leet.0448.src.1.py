class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] and nums[i] != i+1:
                j = nums[i] - 1
                if nums[i] == nums[j]:
                    nums[i] = 0
                    break
                nums[i], nums[j] = nums[j], nums[i]
        return [i+1 for i in range(n) if nums[i] == 0]
