class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            arr = nums[:i] + nums[i+1:]
            yes = True
            for j in range(1, n-1):
                if arr[j] <= arr[j-1]:
                    yes = False
                    break
            if yes:
                return True
        return False
