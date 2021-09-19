class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stk = []
        for x in nums:
            k = bisect.bisect_left(stk, x)
            if k == len(stk):
                stk.append(x)
            elif k >= 0:
                stk[k] = x
        return len(stk)
