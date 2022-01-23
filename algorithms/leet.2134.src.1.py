class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        n1 = nums.count(1)
        acc = sum(nums[:n1])
        nums += nums
        ans = n1 - acc
        for i in range(n1, len(nums)):
            acc += nums[i]
            acc -= nums[i-n1]
            # print(nums[i-n1:i], acc)
            ans = min(ans, n1-acc)
        return ans
