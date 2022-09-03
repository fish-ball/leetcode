class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        a = [nums[0]]
        for i in range(1,n):
            if nums[i] != nums[i-1]:
                a.append(nums[i])
        ans = 0
        n = len(a)
        for i in range(1, n-1):
            if a[i+1] < a[i] > a[i-1] or a[i+1] > a[i] < a[i-1]:
                ans += 1
        return ans
        
