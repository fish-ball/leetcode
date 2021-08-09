class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        i = 0
        last = nums[0]
        ans = 0
        for j, x in enumerate(nums):
            # print(f'{j}, {x}')
            k -= (j - i) * (x - last)
            # print(f'k = {k}')
            last = x
            while k < 0:
                k += last - nums[i]
                i += 1
            ans = max(ans, j - i + 1)
        return ans
