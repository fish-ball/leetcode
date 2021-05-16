class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1<<n):
            acc = 0
            for j in range(n):
                if (1<<j) & i:
                    acc ^= nums[j]
            ans += acc
        return ans
