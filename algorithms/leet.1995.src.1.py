class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i):
                for k in range(j):
                    for l in range(k):
                        if nums[i]-nums[j]-nums[k]-nums[l]==0:
                            ans += 1
        return ans
