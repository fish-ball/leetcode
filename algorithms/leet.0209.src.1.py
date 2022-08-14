class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 0
        i = 0
        acc = 0
        for j, x in enumerate(nums):
            acc += x
            while acc - nums[i] >= target:
                acc -= nums[i]
                i += 1
            if acc >= target:
                if ans == 0 or ans > j - i + 1:
                    ans = j - i + 1
        return ans
