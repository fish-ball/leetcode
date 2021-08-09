class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        a = None
        k = 0
        for x in nums:
            if x == a:
                k += 1
            elif k > 0:
                k -= 1
            else:
                a = x
                k = 1
        if nums.count(a) >= (n+1)//2:
            return a
        return -1
